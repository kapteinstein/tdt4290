import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# TODO: Fix this before deployment - See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/
SECRET_KEY = 'cpivc$!*6-)c(u4k+bw-+cv*j1omilwt)#@#dezn6jb%m)j$y+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

##### APP CONFIGURATION #####
DJANGO_APPS = [
    # Default Django Apps
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rules.apps.AutodiscoverRulesConfig',

    # Admin panel
    'django.contrib.admin',
]

THIRD_PARTY_APPS = [
    'widget_tweaks',
    'django_nose',

    # GraphQL
    'graphene_django',

    # Filtering
    'django_filters',

    # Nested Inlines (admin)
    'nested_admin',
]

LOCAL_APPS = [
    'database',
    #'accounts',
    #'hs',
    #'groups',
    #'forms',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
##### END APP CONFIGURATION #####

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ntnui.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'wsgi.application'

##### DATABASE CONFIGURATION #####

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'dev_database.db'),
    }
}

if os.environ.get('DATABASE_URL'):
    db_from_env = dj_database_url.config(conn_max_age=500)
    DATABASES['default'].update(db_from_env)
    print('Using DB from environment variable.')
else:
    print('Using default file-based DB.')

##### END DATABASE CONFIGURATION #####

##### AUTHENTICATION CONFIGURATION #####

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

AUTH_USER_MODEL = "database.UserModel"

AUTHENTICATION_BACKENDS = (
    'rules.permissions.ObjectPermissionBackend',
    'django.contrib.auth.backends.ModelBackend',
)

##### END AUTHENTICATION CONFIGURATION #####

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'CET'

USE_I18N = True

USE_L10N = True

USE_TZ = True

''' Logging Configuration '''
LOGGING = {
    'version': 1,
    'loggers': {
        'django.db.backends': {
            'level': 'DEBUG',
        },
    },
}


##### STATIC FILE CONFIGURATION #####

STATIC_URL = '/ntnui/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

MEDIA_URL = 'ntnui/static/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'ntnui/static')

##### END STATIC FILE CONFIGURATION #####

##### LOGIN CONFIGURATION #####
LOGIN_REDIRECT_URL = 'home'
LOGIN_URL = 'login'
LOGOUT_REDIRECT_URL = 'login'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# USER settings
DUMMY_USER_EMAIL = 'todd.packer@online.com'
DUMMY_USER_PASSWORD = 'locoloco'

##### END LOGIN CONFIGURATION #####

##### TEST CONFIGURATION #####
# Use nose to run all tests
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

# NOSE_ARGS = [
#    '--with-coverage',
#    '--cover-package=groups, forms, accounts',
#]
##### END TEST CONFIGURATION #####

##### GRAPHENE/GRAPHQL CONFIGURATION #####

GRAPHENE = {
    'SCHEMA': 'data_storage.schema.user_schema'
}

##### END GRAPHENE/GRAPHQL CONFIGURATION #####
