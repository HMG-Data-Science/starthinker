###########################################################################
# 
#  Copyright 2019 Google Inc.
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

import json
from functools import wraps

from django.conf import settings
from django.http import HttpResponseRedirect

from starthinker.util.auth.wrapper import CredentialsFlowWrapper
from starthinker.util.auth import get_client_type


def permission_admin():
  def _decorator(_view):
    @wraps(_view)
    def _wrapper(request, *args, **kwargs):

      # user is logged in
      if request.user.is_authenticated:
        return _view(request, *args, **kwargs)

      # multi user mode, log user in using oauth
      elif settings.UI_CLIENT:
        flow = CredentialsFlowWrapper(settings.UI_CLIENT, redirect_uri=settings.CONST_URL + '/oauth_callback/')
        auth_url, _ = flow.authorization_url(
          prompt='consent',
          #approval_prompt='auto',
          access_type='offline',
          include_granted_scopes='true'
        ) 
        request.session['code_verifier'] = flow.code_verifier
        return HttpResponseRedirect(auth_url)

      # single user mode, no oath, use native django user management ( intead of gsuite )
      else:
        return HttpResponseRedirect('/login/')

    return _wrapper
  return _decorator
