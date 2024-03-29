"""
Django settings for gThink project.

Generated by 'django-admin startproject' using Django 2.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'h%^rr-#khhs3j0&$7q9%u$2jymbe=0p7v^-g%=mvvnlb$0939e'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['www.gthinkinventors.in', 'gthinkinventors.in', '*']  # 'allnew-env.eba-mmj3qtva.ap-south-1.elasticbeanstalk.com', 'secound.ap-south-1.elasticbeanstalk.com', '*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'Api',
    'rest_framework',
    # 'oauth2_provider',
    # 'corsheaders',
    # 'allauth',
    # 'allauth.account',
    # 'allauth.socialaccount',
    # 'allauth.socialaccount.providers.google',
    # 'crispy_forms',
    #  'social_django',
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'oauth2_provider.middleware.OAuth2TokenMiddleware',
]
CORS_ORIGIN_ALLOW_ALL = True
TEST_WITHOUT_MIGRATIONS_COMMAND = 'django_nose.management.commands.test.Command'
ROOT_URLCONF = 'gThink.urls'
LOGIN_URL = '/admin/login/'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', 'lalithkumargoona@gmail.com')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', 'Gthink65!G')
EMAIL_RECEPIENTS = os.environ.get('EMAIL_RECEPIENTS', 'lalithkumargoona@gmail.com')
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    # 'DEFAULT_PERMISSION_CLASSES': [
    #     'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    # ]
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'gThink.wsgi.application'
SOCIAL_AUTH_TWITTER_KEY = 'bDNG23jqQAmEvqTnbkVQbSSyO'
SOCIAL_AUTH_TWITTER_SECRET = 'KUlXQEFFd1TxtKZo4RECeSEmXxwq2qEUG9lNx7IAijyQSHdpWH'
# AUTH_USER_MODEL='Api.Userdata'
# Fetching AWS Environment variables
IP = os.environ.get('IP', 'lalith.gthinkinventors.in')
IP_PORT = os.environ.get('IP_PORT', '1883')
MQTT_SCHEDULING = os.environ.get('MQTT_scheduling', '/Skd')
MQTT_GROUPING = os.environ.get('MQTT_grouping', '/Group')
MQTT_TIMER = os.environ.get('MQTT_timer', '/Timer')
AUTH_KEY = os.environ.get('AUTH_KEY', 'gthink1234')
ACCESS_KEY = os.environ.get('Access_Key', 'AKIAJGY6KRVNY6LEOI4Q')
SECRET_ACCESS_KEY = os.environ.get('Secret_Key', '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')
ENCRPT = os.environ.get('apnd', 'G')
ALL_ON = os.environ.get('all_on', '11')
ALL_OFF = os.environ.get('all_off', '00')
SKD = os.environ.get('Skd', 'skd')
TIME = os.environ.get('Time', 'timer')
# LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'home'
# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'postgres',
#         'USER': 'postgres',
#         'PASSWORD': 'Asdfghjkl65!',
#         'HOST': 'postgres.cdku24fcfmnu.ap-south-1.rds.amazonaws.com',
#         'PORT': '5432',
#     }
# }
#
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'lalith65!G',
        'HOST': 'database-2.c65vpk1rq8r0.us-east-1.rds.amazonaws.com',
        'PORT': '5432',
    }
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'postgres',
#         'USER': 'lalith',
#         'PASSWORD': 'lalith65!',
#         'HOST': 'database-1.cr93vflj9z24.ap-south-1.rds.amazonaws.com',
#         'PORT': '5432',
#     }
# }
# AUTHENTICATION_BACKENDS = (
#     'django.contrib.auth.backends.ModelBackend',
#
#     # `allauth` specific authentication methods, such as login by e-mail
#     'allauth.account.auth_backends.AuthenticationBackend',
#     'social_core.backends.github.GithubOAuth2',
#     'social_core.backends.twitter.TwitterOAuth',
#     'social_core.backends.facebook.FacebookOAuth2',
#     'django.contrib.auth.backends.ModelBackend',
#     'oauth2_provider.backends.OAuth2Backend',
# )

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


SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
            'phone',
        ],
        'AUTH_PARAMS': {
            'access_type': 'offline',
        }
    }
}

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = False

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'gThink/static'
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SITE_ID = 1
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
# STATIC_ROOT = os.path.join(BASE_DIR, "static")
# STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

ACCOUNT_LOGOUT_REDIRECT_URL = 'account_login'

ACCOUNT_EMAIL_REQUIRED = True

SOCIALACCOUNT_QUERY_EMAIL = True

ACCOUNT_SESSION_REMEMBER = True
