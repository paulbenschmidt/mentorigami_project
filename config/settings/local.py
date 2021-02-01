from .base import *

DEBUG = True


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mentorigami',
        'USER': 'postgres',
        'PASSWORD': get_secret('POSTGRES_PASSWORD'),
        'HOST': 'localhost',
        'PORT': 5432,
    }
}


# INSTALLED_APPS += ['debug_toolbar', ]
