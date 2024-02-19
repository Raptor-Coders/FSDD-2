"""
Django settings for coursera project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# For reading Postgres database URL
import dj_database_url

load_dotenv()

# comment added by Paul
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-bg8m$di@e^@802)h(*n5zi133xlhy+#uhlnj_&+va#t@u@^ksk'


SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = os.environ.get("DEBUG", "False").upper() == "TRUE"
LOCAL = os.environ.get("LOCAL", "False").upper() == "TRUE"

SECURE_SSL_REDIRECT = os.environ.get("SECURE_SSL_REDIRECT", "True").upper() == "TRUE"
SESSION_COOKIE_SECURE = os.environ.get("SESSION_COOKIE_SECURE", "True").upper() == "TRUE"
CSRF_COOKIE_SECURE = os.environ.get("CSRF_COOKIE_SECURE", "True").upper() == "TRUE"
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO").upper()

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "")
if ALLOWED_HOSTS:
    ALLOWED_HOSTS = [x.strip() for x in ALLOWED_HOSTS.split(",")]
else:
    ALLOWED_HOSTS = []

CSRF_TRUSTED_ORIGINS = os.environ.get("CSRF_TRUSTED_ORIGINS", "")
if CSRF_TRUSTED_ORIGINS:
    CSRF_TRUSTED_ORIGINS = [x.strip() for x in CSRF_TRUSTED_ORIGINS.split(",")]
else:
    CSRF_TRUSTED_ORIGINS = []




INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',

    'rest_framework',
    
    'courses.apps.CoursesConfig',
    'countries.apps.CountriesConfig',
    'students.apps.StudentsConfig',
    'email_subscriptions.apps.EmailSubscriptionsConfig',
    'contacts.apps.ContactsConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',

    "corsheaders.middleware.CorsMiddleware",

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
]

ROOT_URLCONF = 'coursera.urls'

WSGI_APPLICATION = 'coursera.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {"default": dj_database_url.config(conn_max_age=600, ssl_require=not LOCAL)}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL')


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# For serving Angular files
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
STATIC_URL = "/ng/"
# Path to Angular
ANGULAR_APP_DIR = f'{os.path.abspath(os.path.dirname(__name__))}/my-app/dist/my-app'
WHITENOISE_ROOT = ANGULAR_APP_DIR
WHITENOISE_INDEX_FILE = True

STATICFILES_DIRS = [
    os.path.join(ANGULAR_APP_DIR),
    os.path.join(BASE_DIR, "static"),
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
CORS_ORIGIN_WHITELIST = os.environ.get("CORS_ORIGIN_WHITELIST", "").split(",")

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication'
    ]
}


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        "DIRS": [
            ANGULAR_APP_DIR
        ],
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