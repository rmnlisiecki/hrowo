"""
Django settings for Samochody2 project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '76=(d18*1o#*%fnc(fban97ox$*ajy=vyrlsj-991kv-s#tn3q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'Samochody2.urls'

WSGI_APPLICATION = 'Samochody2.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

#DATABASES = {
#    'default': {
#        'DATABASE_ENGINE': 'django.db.backends.mysql',
#        'DATABASE_NAME': 'all_sports',
#        'DATABASE_HOST': '127.0.0.1',   # Or an IP Address that your DB is hosted on
#        'DATABASE_PORT': '3306',
#        'DATABASE_USER': 'root',
#        'DATABASE_PASSWORD': 'r19l87r19l87',
#    }
#}


#DATABASES = {
#    'default': {
#        'DATABASE_ENGINE': 'django.db.backends.mysql',
#        'DATABASE_NAME': 'languoco_database',
#        'DATABASE_USER': 'languoco_user@localhost',
#        'DATABASE_PASSWORD': 'r19l87r19l87',
#        'DATABASE_HOST': '185.38.249.11',   # Or an IP Address that your DB is hosted on
#        'DATABASE_PORT': '',
#    }
#}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

TEMPLATE_DIRS = (os.path.join(BASE_DIR,  'templates'),)

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
