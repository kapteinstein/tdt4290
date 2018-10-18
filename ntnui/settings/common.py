import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

APP_DIR = os.path.join(BASE_DIR, 'apps')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

SECRET_KEY = os.environ.get('NTNUI_SECRET_KEY')

# If prod is set in env, debug is turned off
DEBUG = "NTNUI_PROD" not in os.environ

ALLOWED_HOSTS = ['.ntnui.no', 'localhost']

##### APP CONFIGURATION #####
DJANGO_APPS = [
    # Default Django Apps
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Admin panel
    'django.contrib.admin',
]

THIRD_PARTY_APPS = [
    'widget_tweaks',
    'django_nose',

    # GraphQL
    'graphene_django',

    # Nested Inlines (admin)
    'nested_admin',

    # Imagekit
    'imagekit',

    # Kundestyrt 2018
    'polymorphic',
]

LOCAL_APPS = [
    'api',
    'authentication',
    'database',
    'management',
    'forms',

    #'accounts',
    #'hs',
    #'groups',
]

INSTALLED_APPS = LOCAL_APPS + THIRD_PARTY_APPS + DJANGO_APPS
##### END APP CONFIGURATION #####

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'authentication.middleware.AuthRequiredMiddleware',
]

ROOT_URLCONF = 'ntnui.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': (
            # It is important that we load the base templates first
            os.path.join(BASE_DIR, 'static', 'templates'),

            # Load app templates
            os.path.join(APP_DIR, 'authentication', 'templates'),
            os.path.join(APP_DIR, 'management', 'templates'),
        ),
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


##### STATIC FILE CONFIGURATION #####

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

##### END STATIC FILE CONFIGURATION #####

###### MESSAGE STORAGE CONFIGURATION ######

MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

###### END MESSAGE STORAGE CONFIGURATION #####

##### MAILGUN SETTINGS #####

#EMAIL_HOST = 'smtp.mailgun.org'
#EMAIL_PORT = 587
#EMAIL_HOST_USER = 'postmaster@mg.ntnui.no'
#EMAIL_HOST_PASSWORD = os.environ.get('MAILGUN_PASSWORD')
#EMAIL_USE_TLS = True


##### LOGIN CONFIGURATION #####
LOGIN_URL = "/a/login"
LOGIN_REDIRECT_URL = '/m/home'
LOGOUT_REDIRECT_URL = '/m/home'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

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
    'SCHEMA': 'database.schema.user_schema'
}

##### END GRAPHENE/GRAPHQL CONFIGURATION #####
