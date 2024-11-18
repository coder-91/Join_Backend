import os
from pathlib import Path
from dotenv import load_dotenv
from google.cloud import secretmanager

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


def get_secret(secret_id):
    environment = os.getenv('JOIN_ENVIRONMENT')

    if environment == 'local':
        value = os.getenv(secret_id)
        if value is None:
            raise ValueError(f"Environment variable '{secret_id}' not found.")
        return value
    else:
        client = secretmanager.SecretManagerServiceClient()
        project_id = 'projects-438313'
        secret_path = f"projects/{project_id}/secrets/{secret_id}/versions/latest"
        try:
            secret = client.access_secret_version(name=secret_path)
            return secret.payload.data.decode("UTF-8")
        except Exception as e:
            raise ValueError(f"Error accessing secret '{secret_id}': {str(e)}")


# Load the environment variables from the .env file
if os.getenv('JOIN_ENVIRONMENT', 'local') == 'local':
    load_dotenv()

ENVIRONMENT = get_secret('JOIN_ENVIRONMENT')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_secret('JOIN_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = get_secret('JOIN_DEBUG') == 'True'

ALLOWED_HOSTS = [host.strip() for host in get_secret('JOIN_ALLOWED_HOSTS').split(',')]

CORS_ALLOWED_ORIGINS = [origin.strip() for origin in get_secret('JOIN_CORS_ALLOWED_ORIGINS').split(',')]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework.authtoken',
    'user',
    'task',
    'subtask',
    'rest_framework',
    'drf_spectacular',
    'corsheaders',
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
]

ROOT_URLCONF = 'Join_Backend.urls'

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

WSGI_APPLICATION = 'Join_Backend.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ORIGIN_ALLOW_ALL = False

AUTH_USER_MODEL = 'user.User'

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    "SCHEMA_PATH_PREFIX": "/api/"
}
