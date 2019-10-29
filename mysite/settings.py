
# Build paths: os.path.join(BASE_DIR, ...)

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#
#
# -------------------------------------SECURITY WARNING--------------
SECRET_KEY = '##CHANGE_ME###'
DEBUG = True
ALLOWED_HOSTS = ['*']
# [staticurl]
STATIC_URL = 'https://storage.googleapis.com/<your-gcs-bucket>/static/'
# [staticurl]
STATIC_ROOT = 'static/'
# -------------------------------------SECURITY WARNING---------------
#
#
###############################################Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles', 
    'polls'
)
MIDDLEWARE = (
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
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
WSGI_APPLICATION = 'mysite.wsgi.application'
ROOT_URLCONF = 'mysite.urls'
#####################################################################
##################################################################### [DATABASE CONFIG]
DATABASES = {
    'default': {
      # 'ENGINE': 'django.db.backends.mysql',
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'default',
        'USER': os.getenv('DATABASE_USER'),           #EXPOT DATABASES_USER=
        'PASSWORD': os.getenv('DATABASE_PASSWORD'),    #EXPORT DATABASES_PASSWORD=
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
####################################################################
##################################################################### [DETAIL CONFIG]
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True