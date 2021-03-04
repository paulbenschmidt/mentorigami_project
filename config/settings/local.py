from .base import *

DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mentorigami',
        'USER': get_secret('USER'),
        'PASSWORD': get_secret('POSTGRES_PASSWORD'),
        'HOST': get_secret('LOCAL_HOST'),
        'PORT': get_secret('PORT'),
    }
}

# INSTALLED_APPS += ['debug_toolbar', ]
