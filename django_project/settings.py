import os
from pathlib import Path
from decouple import config

# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Security settings
SECRET_KEY = config('SECRET_KEY', default='django-insecure-na_i!_poqmi%#b$a(2a75!4xx$v4hjjpss5nmty$0rtlrp3h^p')
DEBUG = config('DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = [
    'app-tditmans-5.devedu.io',
    '127.0.0.1',
    'localhost',
]

# Login settings
LOGIN_URL = '/login/'

# Password reset token timeout in seconds (1 day)
PASSWORD_RESET_TIMEOUT = 86400

# Installed apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'django_apscheduler',
    'filmproject.apps.FilmprojectConfig',  # Custom app
    'rest_framework',
    'django-cleanup', # Cleaning up files
]

# Authentication backends
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

# CSRF and CORS settings
CSRF_TRUSTED_ORIGINS = [
    'https://app-tditmans-5.devedu.io',
]
CORS_ALLOW_ALL_ORIGINS = True

# Middleware configuration
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URL configuration
ROOT_URLCONF = 'django_project.urls'

# Template settings
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

# WSGI application
WSGI_APPLICATION = 'django_project.wsgi.application'

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files configuration
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'filmproject/static')]

# Media files configuration
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'filmproject/media')

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Email configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = config('GOOGLE_MAIL_ADDRESS', default='your-email@gmail.com')
EMAIL_HOST_PASSWORD = config('GOOGLE_MAIL_PASSWORD', default='your-password')
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# Scheduler and logging configuration
DJANGO_CRON_CLASSES = [
    'filmproject.cron_jobs.DatabaseCleanupCronJob',
]

# Add flag to prevent duplicate scheduler starts
SCHEDULER_RUNNING = False  # Flag to prevent multiple scheduler starts

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'filmproject': {
            'handlers': ['console'],
            'level': 'INFO',
        },
    },
}