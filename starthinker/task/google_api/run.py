###########################################################################
#
#  Copyright 2020 Google LLC
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
###########################################################################

"""Moves data to and from Google Rest API and BigQuery.

Intended to be thin and pass control to recipe JSON for flexibility.
Task designed to be used with a recipe.
Leverages discovery document to define schema.
The results and error sections are optional.

For invocation see:
scripts/google_api_to_bigquery.json

Example Read DV360 Partner Name and Id Into BigQuery:

   { "google_api": {
      "auth": "user",
      "api": "displayvideo",
      "version": "v1",
      "function": "partners.list",
      "kwargs": {"fields":"partners.displayName,partners.partnerId,nextPageToken"},
      "results": {
        "bigquery": {
          "dataset": "DV_Barnacle",
          "table": "DV_Partners"
        }
      }
    }}

Example Read DV360 Advertisers defined in another BigQuery table:

    { "google_api": {
      "auth": "user",
      "api": "displayvideo",
      "version": "v1",
      "function": "advertisers.lineItems.list",
      "kwargs_remote":{
        "bigquery":{
          "dataset":"DV_Targeting_Audit",
          "query":"SELECT CAST(advertiserId AS STRING) AS advertiserId FROM `DV_Targeting_Audit.DV_Advertisers`;",
          "legacy":false
        }
      },
      "iterate":true,
      "results": {
        "bigquery": {
          "dataset": "DV_Targeting_Audit",
          "table": "DV_LineItems"
        }
      }
    }}

Example Write Insertion Orders into DV360 from BigQuery:

    { "google_api": {
      "auth": "user",
      "api": "displayvideo",
      "version": "v1",
      "function": "advertisers.insertionOrders.patch",
      "kwargs_remote":{
        "bigquery":{
          "dataset":"CM_DV_Demo",
          "table":"DV_IO_Patch"
        }
      },
      "results": {
        "bigquery": {
          "dataset": "CM_DV_Demo",
          "table": "DV_IO_Patch_Results"
        }
      },
      "errors": {
        "bigquery": {
          "dataset": "CM_DV_Demo",
          "table": "DV_IO_Patch_Errors"
        }
      }
    }}
"""

from googleapiclient.errors import HttpError

from starthinker.util.bigquery import table_create
from starthinker.util.data import get_rows
from starthinker.util.data import put_rows
from starthinker.util.cm import get_profile_for_api
from starthinker.util.google_api import API
from starthinker.util.discovery_to_bigquery import Discovery_To_BigQuery


ERROR_SCHEMA = [
  { 'name': 'Error', 'type': 'STRING', 'mode': 'NULLABLE' },
  { 'name': 'Parameters', 'type': 'RECORD', 'mode': 'REPEATED', 'fields': [
    { 'name': 'Key', 'type': 'STRING', 'mode': 'NULLABLE' },
    { 'name': 'Value', 'type': 'STRING', 'mode': 'NULLABLE' },
  ]}
]


def google_api_initilaize(config, api_call, alias=None):
  """Some Google API calls require a lookup or pre-call, add it here.

  Modifies the API call before actual execution with any data
  specifically required by an endpoint.  Currently:

    > dfa-reporting - look up user profile and add to call.

  Args:
    api_call (dict): the JSON for the API call as defined in recipe.
    alias (string): mostly used to signal a list behavior (change to iterate in future?)

  Returns (dict):
    A modified JSON with additional API values added.
    Currently mostly used by dfareporting API to add profile and account.

  Raises:
    ValueError: If a required key in the recipe is missing.
  """

  if api_call['function'].endswith('list') or alias == 'list':
    api_call['iterate'] = True

  if api_call['api'] == 'dfareporting':

    if not api_call['function'].startswith('userProfiles'):

      is_superuser, profile_id = get_profile_for_api(
        config, api_call['auth'], api_call['kwargs']['id'] if api_call['function'] == 'accounts.get' else api_call['kwargs']['accountId']
      )
      api_call['kwargs']['profileId'] = profile_id

      if is_superuser:
        from starthinker.util.cm_internalv34_uri import URI as DCM_URI
        api_call['version'] = 'internalv3.3'
        api_call['uri'] = DCM_URI
      elif 'accountId' in api_call['kwargs']:
        del api_call['kwargs']['accountId']


def google_api_build_results(config, auth, api_call, results):
  """Builds the BigQuery table to house the Google API call results.

  Optional piece of the recipe, will create a BigQuery table for results.
  Takes results, which defines a bigquery endpoint, and adds fields.

  Args:
    auth (string): either "user" or "service" to make the BigQuery call.
    api_call (dict): the JSON for the API call as defined in recipe.
    results (dict): defines where the data will be written

  Returns (dict):
    A modified results JSON with additional API values added.

  Raises:
    ValueError: If a required key in the recipe is missing.
  """

  if 'bigquery' in results:

    if 'schema' not in results['bigquery']:
      results['bigquery']['schema'] = Discovery_To_BigQuery(
        api_call['api'],
        api_call['version'],
        api_call.get('key', None),
      ).method_schema(
        api_call['function'],
        api_call.get('iterate', False)
      )

    if 'format' not in results['bigquery']:
      results['bigquery']['format'] = 'JSON'

    results['bigquery']['skip_rows'] = 0

    table_create(
      config,
      results['bigquery'].get('auth', auth),
      config.project,
      results['bigquery']['dataset'],
      results['bigquery']['table'],
      results['bigquery']['schema'],
      overwrite=False
    )

  return results


def google_api_build_errors(config, auth, api_call, errors):
  """Builds the BigQuery table to house the Google API call errors.

  Optional piece of the recipe, will create a BigQuery table for errors.
  Takes errors, which defines a bigquery endpoint, and adds fields.

  Args:
    auth (string): either "user" or "service" to make the BigQuery call.
    api_call (dict): the JSON for the API call as defined in recipe.
    errors (dict): defines where the data will be written

  Returns (dict):
    A modified results JSON with additional API values added.

  Raises:
    ValueError: If a required key in the recipe is missing.
  """

  if 'bigquery' in errors:
    errors['bigquery']['schema'] = ERROR_SCHEMA
    errors['bigquery']['format'] = 'JSON'
    errors['bigquery']['skip_rows'] = 0
    errors['bigquery']['disposition'] = 'WRITE_TRUNCATE'

    table_create(
      config,
      errors['bigquery'].get('auth', auth),
      config.project,
      errors['bigquery']['dataset'],
      errors['bigquery']['table'],
      errors['bigquery']['schema'],
      overwrite=False
    )

  return errors


def google_api_execute(config, auth, api_call, results, errors, limit=None):
  """Execute the actual API call and write to the end points defined.

  The API call is completely defined at this point.
  The results and error definition is optional.

  Args:
    auth (string): either "user" or "service" to make the API call.
    api_call (dict): the JSON for the API call as defined in recipe.
    results (dict): defines where the data will be written
    errors (dict): defines where the errors will be written
    limit (int): Reduce the number of calls ( mostly for debugging )

  Returns (dict):
    None, all data is transfered between API / BigQuery

  Raises:
    ValueError: If a required key in the recipe is missing.
  """


  try:
    rows = API(config, api_call).execute()

    if results:
      # check if single object needs conversion to rows
      if isinstance(rows, dict):
        rows = [rows]

      # check if simple string API results
      elif results.get('bigquery', {}).get('format', 'JSON') == 'CSV':
        rows = [[r] for r in rows]

      if config.verbose:
        print('.', end='', flush=True)

      yield from map(lambda r: Discovery_To_BigQuery.clean(r), rows)

  except HttpError as e:

    if errors:
      rows = [{
          'Error':
              str(e),
          'Parameters': [{
              'Key': k,
              'Value': str(v)
          } for k, v in api_call['kwargs'].items()]
      }]
      put_rows(config, auth, errors, rows)

      if 'bigquery' in errors:
        errors['bigquery']['disposition'] = 'WRITE_APPEND'

    else:
      raise e


def google_api(config, task):
  """Task handler for recipe, delegates all JSON parameters to functions.

  Executes the following steps:
    1. Define the API call.
    2. Define the results destination.
    3. Define the error destination.

  The results table for BigQuery is created first as blank, this allows
  writes from multiple API calls to aggregate into a single table.

  The API call can be specified via kwargs or kwargs_remote.
    kwargs - hard coded values for the API call as a dictionary.
    kwargs_remote - values loaded from a source such as BigQuery.

  Args:
    None, all parameters are exposed via task.

  Returns:
    None, all data is read and written as a side effect.

  Raises:
    ValueError: If a required key in the recipe is missing.
  """

  if config.verbose:
    print(
      'GOOGLE_API',
      task['api'],
      task['version'],
      task['function']
    )

  api_call = {
    'auth': task['auth'],
    'api': task['api'],
    'version': task['version'],
    'function': task['function'],
    'iterate': task.get('iterate', False),
    'limit': task.get('limit', None),
    'key': config.key,
    'headers': task.get('headers'),
  }

  results = google_api_build_results(
    config,
    task['auth'],
    api_call,
    task.get('results', {})
  )

  errors = google_api_build_errors(
    config,
    task['auth'],
    api_call,
    task.get('errors', {})
  )

  # get parameters from JSON
  if 'kwargs' in task:
    kwargs_list = task['kwargs'] if isinstance(
      task['kwargs'], (list, tuple)
    ) else [task['kwargs']]

  # get parameters from remote location ( such as BigQuery )
  elif 'kwargs_remote' in task:
    kwargs_list = get_rows(
      config,
      task['auth'],
      task['kwargs_remote'],
      as_object=True
    )

  # no parameters, ensures at least one call is made
  else:
    kwargs_list = [{}]

  def google_api_combine():
    # loop through paramters and make possibly multiple API calls
    for kwargs in kwargs_list:
      api_call['kwargs'] = kwargs
      google_api_initilaize(config, api_call, task.get('alias'))
      yield from google_api_execute(config, task['auth'], api_call, results, errors, task.get('limit'))

  put_rows(
    config,
    task['auth'],
    results,
    google_api_combine()
  ) # FIX: check auth on nested BQ write
