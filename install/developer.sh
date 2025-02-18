#!/bin/bash

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


test_ui() {

  install_virtualenv;
  install_requirements;
  setup_credentials_service;
  setup_credentials_commandline;
  save_config;

  echo ""
  echo "----------------------------------------"
  echo "Load Development Settings - ${STARTHINKER_ROOT}/starthinker_assets/development.sh"
  echo "----------------------------------------"
  echo ""

  source "${STARTHINKER_ROOT}/starthinker_assets/development.sh";

  echo ""
  echo "----------------------------------------"
  echo "Run UI Tests - python starthinker_ui/manage.py test"
  echo "----------------------------------------"
  echo ""

  echo ""
  echo "Account: python starthinker_ui/manage.py test account"
  echo ""

  python "${STARTHINKER_ROOT}/starthinker_ui/manage.py" test account -v 2;

  echo ""
  echo "Website: python starthinker_ui/manage.py test website"
  echo ""

  python "${STARTHINKER_ROOT}/starthinker_ui/manage.py" test website -v 2;

  echo ""
  echo "Project: python starthinker_ui/manage.py test project"
  echo ""

  python "${STARTHINKER_ROOT}/starthinker_ui/manage.py" test project -v 2;

  echo ""
  echo "Recipe: python starthinker_ui/manage.py test recipe "
  echo ""

  python "${STARTHINKER_ROOT}/starthinker_ui/manage.py" test recipe -v 2;

  deactivate

  echo "Done"
  echo ""
}

test_tasks() {

  install_virtualenv;
  install_requirements;
  setup_credentials_service;
  setup_credentials_commandline;
  save_config;

  echo ""
  echo "----------------------------------------"
  echo "Load Development Settings - ${STARTHINKER_ROOT}/starthinker_assets/development.sh"
  echo "----------------------------------------"
  echo ""

  source "${STARTHINKER_ROOT}/starthinker_assets/development.sh";

  echo ""
  echo "----------------------------------------"
  echo "Run Task Tests - python ${STARTHINKER_ROOT}/starthinker/tool/test.py"
  echo "----------------------------------------"
  echo ""

  python "${STARTHINKER_ROOT}/starthinker/tool/test.py";

  deactivate

  echo "Done"
  echo ""
}


launch_developer_ui() {
  cloud_shell=$1

  install_virtualenv;
  install_requirements;
  setup_credentials_service;
  setup_credentials_commandline;
  save_config;
  make_cron;

  echo ""
  echo "----------------------------------------"
  echo "Load Development Settings - ${STARTHINKER_ROOT}/starthinker_assets/development.sh"
  echo "----------------------------------------"
  echo ""

  source "${STARTHINKER_ROOT}/starthinker_assets/development.sh";

  echo ""
  echo "----------------------------------------"
  echo "Configure Development Database - ${STARTHINKER_ROOT}/starthinker_assets/database.sqlite"
  echo "----------------------------------------"
  echo ""

  python "${STARTHINKER_ROOT}/starthinker_ui/manage.py" makemigrations;
  python "${STARTHINKER_ROOT}/starthinker_ui/manage.py" migrate;

  if [ $cloud_shell == "--cloud_shell" ]; then

    echo "----------------------------------------"
    echo "Launch Cloud Shell UI - python ${STARTHINKER_ROOT}/starthinker_ui/manage.py runserver 0.0.0.0:8000"
    echo "----------------------------------------"
    echo ""

    echo "Step 1: Launch Web Preview"
    echo "----------------------------------------"
    echo "  A. Open Web Preview in upper right of this window, [<>] icon."
    echo "  B. Ensure the PORT is set to 8080 ( default)."
    echo "  C. Click Preview on Port 8080. The server is not running yet, you will get an error."
    echo "  D. Copy the URL and paste it below...."
    echo ""

    read -p "Cloud Shell URL: " url

    STARTHINKER_UI_DOMAIN=$(awk -F/ '{print $3}' <<< $url)

    echo ""
    echo "Step 2: Configure oAuth Callback"
    echo "----------------------------------------"echo
    echo "  A. Visit: https://console.developers.google.com/apis/credentials"
    echo "  B. Edit the client credentials uploaded in an earlier step."
    echo "  C. Under Authorized redirect URIs add: https://$STARTHINKER_UI_DOMAIN/oauth_callback/"
    echo "  D. Click Save."
    echo ""

    read -p "Press enter to continue, then visit the browser at: https://$STARTHINKER_UI_DOMAIN"

  else

    echo "----------------------------------------"
    echo "Launch Developer UI - python ${STARTHINKER_ROOT}/starthinker_ui/manage.py runserver 0.0.0.0:8000"
    echo "----------------------------------------"
    echo ""


  fi

  python "${STARTHINKER_ROOT}/starthinker_ui/manage.py" runserver 0.0.0.0:8000
  deactivate

  echo ""
  echo "Done"
  echo ""
}

launch_developer_worker() {
  options=$1

  echo "----------------------------------------"
  echo "Launch Developer Worker - python ${STARTHINKER_ROOT}/starthinker_ui/manage.py job_worker --verbose ${options}"
  echo "----------------------------------------"
  echo ""

  source "${STARTHINKER_ROOT}/starthinker_assets/development.sh";
  python "${STARTHINKER_ROOT}/starthinker_ui/manage.py" job_worker --verbose ${options}
  deactivate

  echo ""
  echo "Done"
  echo ""
}


install_developer() {
  install_virtualenv;
  install_requirements;
  setup_credentials_service;
  setup_credentials_commandline;
  setup_credentials_user;
  save_config;
  make_cron;
}

generate_assets() {
  echo ""
  echo "----------------------------------------------------------------------"
  echo "Generate StarThinker Assets"
  echo "----------------------------------------------------------------------"
  echo ""

  python3 -m pip install --upgrade setuptools wheel
  source "${STARTHINKER_ROOT}/starthinker_assets/development.sh";
  python3 starthinker_ui/manage.py colab
  python3 starthinker_ui/manage.py airflow
  python3 starthinker_ui/manage.py example
  python3 starthinker_ui/manage.py github --analytics UA-167283455-3
  deactivate

  echo ""
  echo "Done"
  echo ""
}


function deploy_pypi() {

  echo ""
  echo "----------------------------------------------------------------------"
  echo "PyPi StarThinker $1"
  echo "----------------------------------------------------------------------"
  echo ""
  echo "Optional, create the following configuration to avoid a password ask:"
  echo "vim ~/.pipyrc"
  echo "chmod 600 ~/.pipyrc"
  echo ""
  echo "File contents:"
  echo ""
  echo "[distutils]"
  echo "  index-servers="
  echo "    pypi"
  echo "    testpypi"
  echo ""
  echo "[pypi]"
  echo "  username: __token__"
  echo "  password: ???"
  echo ""
  echo "[testpypi]"
  echo "  repository: https://test.pypi.org/legacy/"
  echo "  username: __token__"
  echo "  password: ???"
  echo ""

  repository="testpypi"
  if [ $1 = "--production" ]; then
    repository="pypi"
  fi

  python3 -m pip install --upgrade setuptools wheel
  rm -rf "${STARTHINKER_ROOT}/dist"
  rm -rf "${STARTHINKER_ROOT}/build"
  python3 setup.py sdist bdist_wheel
  python3 -m pip install --upgrade twine
  python3 -m twine upload --verbose --repository ${repository} dist/*

  echo ""
  echo "Done"
  echo ""
}


setup_developer() {
  echo ""
  echo "------------------------------------------------------------------------------"
  echo ""
  echo "Developer Setup"
  echo ""
  echo "------------------------------------------------------------------------------"
  echo ""
  echo "This script manages environmental settings for StarThinker. you can edit them"
  echo "manually from the command line or use this script to manage them. All settings are in:"
  echo " - $STARTHINKER_CONFIG"
  echo ""
  echo "This script or you may create or modify:"
  echo "  - $STARTHINKER_ROOT/starthinker_assets/config.sh"
  echo "  - $STARTHINKER_ROOT/starthinker_assets/database.sqlite"
  echo ""
  echo "After running this script once, activate StarThinker development settings from the command line:"
  echo " - source $STARTHINKER_ROOT/starthinker_assets/development.sh"
  echo ""
  echo "Or activate production settings from the command line:"
  echo " - source $STARTHINKER_CONFIG"
  echo ""
  echo "After activating StarThinker run the sample code:"
  echo " - python starthinker/all/run.py starthinker/gtech/say_hello.json -u \$STARTHINKER_USER -s \$STARTHINKER_SERVICE -p \$STARTHINKER_PROJECT"
  echo ""
  echo "After activating StarThinker run the UI from the menu below or from the command line:"
  echo " - source $STARTHINKER_ROOT/starthinker_assets/developmnet.sh"
  echo " - python starthinker_ui/manage.py runserver 0.0.0.0:8000"
  echo ""
  echo "Deactivate the virtual environment:"
  echo " - deactivate"
  echo ""

  developer_done=0
  developer_options=("Install Developer StarThinker" "Launch Developer UI" "Launch Cloud Shell UI" "Developer Worker - Single" "Developer Worker - Peristent" "Test UI" "Test Tasks" "Generate Dags Colabs And Docs" "Generate Translations" "Deploy Test PyPi", "Deploy Production PyPi")

  while (( !developer_done ))
  do
    echo "----------------------------------------------------------------------"
    echo "Developer Menu"
    echo "----------------------------------------------------------------------"
    echo ""

    PS3='Your Choice ( q = Quit ): '
    select developer_option in "${developer_options[@]}"; do
      case $REPLY in
        1) install_developer; break;;
        2) launch_developer_ui; break;;
        3) launch_developer_ui "--cloud_shell"; break;;
        4) launch_developer_worker "--test"; break;;
        5) launch_developer_worker ""; break;;
        6) test_ui; break;;
        7) test_tasks; break;;
        8) generate_assets; break;;
        9) generate_translations; break;;
        10) deploy_pypi "--test"; break;;
        11) deploy_pypi "--production"; break;;
        q) developer_done=1; break;;
        *) echo "What's that?";;
      esac
    done
    echo ""
  done
}


if [ "$1" = "--instance" ];then
  shift;

  if [ -d "${PWD}/install" ]; then

    THIS_DIR=$PWD
    source ${THIS_DIR}/install/config.sh

    setup_developer;

  else

    echo ""
    echo "Directory starthinker not found."
    echo "This utility must be run from the StarThinker directory containing the install folder."
    echo "Please change directories and try again."
    echo ""

  fi
fi
