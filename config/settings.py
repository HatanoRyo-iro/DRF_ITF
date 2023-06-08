"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-4)q^$bg1jjhire)qghjyu$$2ss+&osg$g0psden_*iai2x!ktm"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'rest_framework',
    'rest_framework.authtoken',
    'api.apps.ApiConfig',
    'accounts.apps.AccountsConfig',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

REST_FRAMEWORK ={
    'DEFAULT_THROTTLE_CLASSES' : [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES' : {
        'anon' : '10/minute',
        'user' : '1000/hour',
    },
    'DEFAULT_AUTHENTICATION_CLASSES' : [
        'rest_framework.authentication.TokenAuthentication',
    ],
}

DEFAULTS = {
    # Base API policies
    'DEFAULT_RENDERER_CLASSES' : [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    'DEFAULT_PARSER_CLASSES' : [
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES' : [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES' : [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_THROTTLE_CLASSES' : [],
    'DEFAULT_CONTENT_NEGOTIATION_CLASS' : 'rest_framework.negotiation.DefaultContentNegotiation',
    'DEFAULT_METADATA_CLASS' : 'rest_framework.metadata.SimpleMetadata',
    'DEFAULT_VERSIONING_CLASS' : 'rest_framework.versioning.URLPathVersioning',
    
    # Generic view behavior
    'DEFAULT_PAGINATION_CLASS' : None,
    'DEFAULT_FILTER_BACKENDS' : [],
    
    # Schema
    'DEFAULT_SCHEMA_CLASS' : 'rest_framework.schemas.AutoSchema',
    
    # Throttling
    'DEFAULT_THROTTLE_RATES' : {
        'user' : None,
        'anon' : None,
    },
    'NUM_PROXIES' : None,
    
    # Pagination
    'PAGE_SIZE' : None,
    
    # Filtering
    'SEARCH_PARAM' : 'search',
    'ORDERING_PARAM' : 'ordering',
    
    # Versioning
    'DEFAULT_VERSION' : None,
    'ALLOWED_VERSIONS' : None,
    'VERSION_PARAM' : 'version',
    
    # Authentication
    'UNAUTHENTICATED_USER' : 'django.contrib.auth.models.AnonymousUser',
    'UNAUTHENTICATED_TOKEN' : None,
    
    # View configuration
    'VIEW_NAME_FUNCTION' : 'rest_framework.views.get_view_name',
    'VIEW_DESCRIPTION_FUNCTION' : 'rest_framework.views.get_view_description',
    
    # Exception handling
    'EXCEPTION_HANDLER' : 'rest_framework.views.exception_handler',
    'NON_FIELD_ERRORS_KEY' : 'non_field_errors',
}