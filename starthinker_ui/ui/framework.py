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
"""This is a technical settings file that needs to be extended with additional settings.

   Django Specific Documentation:
     - Generated by 'django-admin startproject' using Django 1.11.1.
     - For more information on this file, see:
     https://docs.djangoproject.com/en/1.11/topics/settings/
     - For the full list of settings and their values, see:
     https://docs.djangoproject.com/en/1.11/ref/settings/
     - For production, see:
     https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

"""

import os

from django.utils.translation import gettext_lazy as _

ADMIN_ENABLED = False

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    #'django.contrib.staticfiles',
    'starthinker_ui.account.apps.AccountConfig',
    'starthinker_ui.recipe',
    'starthinker_ui.project',
    'starthinker_ui.website',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Relative to current application load
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR + '/templates/',],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
            'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME':
            'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME':
            'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME':
            'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

LOCALE_PATHS = [
  BASE_DIR + '/translations/',
]

LANGUAGES = [
  ('en', _('English')),
  ('es', _('Spanish')),
  ('es-419', _('Spanish - LATAM')),
  ('fr', _('French')),
  ('fr-ca', _('French Candian')),
  ('hi', _('Hinid')),
  ('pl', _('Polish')),
  ('pt', _('Portuguese')),
]

USE_I18N = True
USE_L10N = True
USE_TZ = False

DEFAULT_CHARSET = 'utf-8'
DEFAULT_AUTO_FIELD='django.db.models.AutoField'

# User
AUTH_USER_MODEL = 'account.Account'

# Application Handler Maps
ROOT_URLCONF = 'starthinker_ui.ui.urls'
WSGI_APPLICATION = 'starthinker_ui.ui.wsgi.application'
