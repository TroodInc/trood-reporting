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
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'core.middlewares.TroodAuth',
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

DATABASES = {'default': env.db()}
DATABASES['default']['CONN_MAX_AGE'] = 500

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False

STATIC_ROOT = root('static')
STATIC_URL = '/reporting/static/'

# STATICFILES_DIRS = (root('static'),)

MEDIA_URL = '/media/'
MEDIA_ROOT = root('media')

AUTHENTICATION_BACKENDS = ['core.backends.TroodAuth']

AUTH_URL = env('AUTH_URL')

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('core.permissions.TroodAuth', ),
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.NamespaceVersioning',
    'DEFAULT_RENDERER_CLASSES': ('rest_framework.renderers.JSONRenderer', ),
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

# Sentry
if env('SENTRY_ENABLED'):
    RAVEN_CONFIG = {
        'dsn': env('SENTRY_DSN'),
        'release': env('SENTRY_ENV'),
    }
