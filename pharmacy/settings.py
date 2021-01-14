"""
Django settings for pharmacy project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import configparser
import os
from django.conf import settings
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

APP_NAME = 'pharmacy'
SITE_ID = 1

ETC_DIR = '/etc/pharmacy/'

LOGIN_REDIRECT_URL = 'home_url'

INDEX_PAGE = 'edc-pharma.bhp.org.bw:8000'
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'sdjsvamxjn)p^p7a)n5-2&+y7&2n92ivw*)$%fzt#o@o1igmi6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', 'pharma-dev.bhp.org.bw', '127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django_crypto_fields.apps.AppConfig',
    'edc_dashboard.apps.AppConfig',
    'edc_device.apps.AppConfig',
    'edc_navbar.apps.AppConfig',
    'edc_timepoint.apps.AppConfig',
    'pharma_dashboard.apps.AppConfig',
    'pharma_subject.apps.AppConfig',
    'pharmacy.apps.AppConfig',
    'pharmacy.apps.EdcLabelAppConfig',
    'pharmacy.apps.EdcBaseAppConfig'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'edc_dashboard.middleware.DashboardMiddleware',
    'edc_subject_dashboard.middleware.DashboardMiddleware',
]

ROOT_URLCONF = 'pharmacy.urls'

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

WSGI_APPLICATION = 'pharmacy.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

mysql_config = configparser.ConfigParser()
mysql_config.read(os.path.join(ETC_DIR, 'mysql.ini'))

HOST = mysql_config['mysql']['host']
DB_USER = mysql_config['mysql']['user']
DB_PASSWORD = mysql_config['mysql']['password']
DB_NAME = mysql_config['mysql']['database']
PORT = mysql_config['mysql']['port']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
        'HOST': HOST,   # Or an IP Address that your DB is hosted on
        'PORT': PORT,
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_CODE = '1'
DEFAULT_STUDY_SITE = '1'
REVIEWER_SITE_ID = 41

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'pharmacy', 'static')

CUPS_SERVERS = 'localhost'
LABEL_PRINTER = 'pharma_test_printer'
LABEL_TEMPLATE_FOLDER = os.path.join(
        settings.STATIC_ROOT, APP_NAME, 'label_templates')


DASHBOARD_URL_NAMES = {
    'patient_listboard_url': 'pharma_dashboard:patient_listboard_url',
    'dispense_listboard_url': 'pharma_dashboard:dispense_listboard_url',
    'data_manager_listboard_url': 'edc_data_manager:data_manager_listboard_url',
}

DASHBOARD_BASE_TEMPLATES = {
    'listboard_base_template': 'pharmacy/base.html',
    'patient_listboard_template': 'pharma_dashboard/listboard.html',
    'dispense_listboard_template': 'pharma_dashboard/dispensary/listboard.html',
    'data_manager_listboard_template': 'edc_data_manager/listboard.html',
}
