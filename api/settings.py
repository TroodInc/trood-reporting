import os

import dj_database_url
import environ

# Django environ
root = environ.Path(__file__) - 2
env = environ.Env(
    DEBUG=(bool, True),
    SECRET_KEY=(str, '&43a$!xv3gsfds(41+1=rh3mt1*gi5wc3c$_wnj_)j7c%lf&#1'),
    SENTRY_ENABLED=(bool, False),
    SENTRY_DSN=(str, 'https://b929140809d441b98f4ba197b2560d0e:8929448bcde043e48d712dbcd11d0794@sentry.tools.trood.ru/4'),
    SENTRY_ENV=(str, 'dev'),
    AUTH_URL=(str, 'http://authorization:8000/api/v1.0'),
    API_URL=(str, 'http://0.0.0.0:8000/'),
)

environ.Env.read_env(env_file=root('.env'))

BASE_DIR = root()

SECRET_KEY = env('SECRET_KEY')

DEBUG = env('DEBUG')

API_URL = env('API_URL')

# ALLOWED_HOSTS = ['*.trood.ru', ]
# if DEBUG:
#     ALLOWED_HOSTS.append('*')
ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',

    'rest_framework',
    'drf_yasg',
    'raven.contrib.django.raven_compat',
    'django_extensions',

    'trood_reporting',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'api.urls'

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

WSGI_APPLICATION = 'api.wsgi.application'

USE_X_FORWARDED_HOST = True


DATABASES = {
    'default': dj_database_url.config(
        default='pgsql://reporting:reporting@reporting_postgres/reporting')
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False

STATIC_ROOT = root('static')
STATIC_URL = '/reporting/static/'


MEDIA_URL = '/media/'
MEDIA_ROOT = root('media')

AUTHENTICATION_BACKENDS = ['core.backends.TroodAuth']

AUTH_URL = env('AUTH_URL')

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework.filters.OrderingFilter',
        'rest_framework.filters.SearchFilter',
        'trood.contrib.django.filters.TroodRQLFilterBackend',
    ),
    'DEFAULT_PAGINATION_CLASS': 'trood.contrib.django.pagination.TroodRQLPagination',
}


SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Token': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    }
}

AUTH_TYPE = os.environ.get('AUTHENTICATION_TYPE')

if AUTH_TYPE == 'NONE':
    REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES'] = ()
    REST_FRAMEWORK['DEFAULT_PERMISSION_CLASSES'] = ()
elif AUTH_TYPE == 'TROOD':
    TROOD_AUTH_SERVICE_URL = os.environ.get(
      'TROOD_AUTH_SERVICE_URL', 'http://authorization.trood:8000/'
    )
    AUTH_URL = TROOD_AUTH_SERVICE_URL
    TROOD_ABAC = {
        'RULES_SOURCE': os.environ.get("ABAC_RULES_SOURCE", "URL"),
        'RULES_PATH': os.environ.get("ABAC_RULES_PATH", "{}api/v1.0/abac/".format(TROOD_AUTH_SERVICE_URL))
    }
    SERVICE_DOMAIN = os.environ.get("SERVICE_DOMAIN", "REPORTING")
    SERVICE_AUTH_SECRET = os.environ.get("SERVICE_AUTH_SECRET")

    REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES'] = (
        'trood.contrib.django.auth.authentication.TroodTokenAuthentication',
    )

    MIDDLEWARE += [
        'trood.contrib.django.auth.middleware.TroodABACMiddleware',
        'core.middlewares.TroodAuth',
    ]

    REST_FRAMEWORK['DEFAULT_PERMISSION_CLASSES'] = (
        'trood.contrib.django.auth.permissions.TroodABACPermission',
        'core.permissions.TroodAuth',
    )

    REST_FRAMEWORK['DEFAULT_FILTER_BACKENDS'] += (
        'trood.contrib.django.auth.filter.TroodABACFilterBackend',
    )
