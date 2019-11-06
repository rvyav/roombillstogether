"""
Django settings for roombillstogether project.

Generated by 'django-admin startproject' using Django 2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
from .prod_settings import (
    SAFE,
    DB_NAME,
    DB_PASSWORD,
    ACCOUNT_SID_KEY,
    AUTH_TOKEN_KEY,
    PHONE_NUMBER_KEY
)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = [SAFE]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'users',
    'core',
    'crispy_forms',
    'twilio',
    'phonenumber_field',
    'phonenumbers',
    'django_celery_beat',
    'sorl.thumbnail',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'roombillstogether.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'roombillstogether.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DB_NAME,
        'USER': 'postgres',
        'PASSWORD': DB_PASSWORD,
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

TIME_ZONE = 'America/New_York'

USE_TZ = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

# Static

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATIC_URL = '/static/'

# STATICFILES_DIRS = (
#         os.path.join(BASE_DIR, 'roombillstogether/static'),

# )

# Store uploaded files

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')        

MEDIA_URL = '/media/'

# CS4

CRISPY_TEMPLATE_PACK = 'bootstrap4'


# User abstraction multi type

AUTH_USER_MODEL = 'users.CustomUser'


# Twilio

ACCOUNT_SID = ACCOUNT_SID_KEY
AUTH_TOKEN = AUTH_TOKEN_KEY
PHONE_NUMBER = PHONE_NUMBER_KEY


# Redirect after login

LOGIN_REDIRECT_URL = 'core:month_list'

# Redirect after logout

LOGOUT_REDIRECT_URL = 'login' 

# Redirect to login if not logged in, decorator

LOGIN_URL = 'login' 



# CELERY

from celery.schedules import crontab

CELERY_BEAT_SCHEDULE = {
    'task-one': {
        'task1': 'core.tasks.send_instant_sms',
        'schedule': crontab(minute=3),
    },
}






