from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'juegoschaco',
        'USER': 'root',
        'PASSWORD': 'Emanuel153456',
        'HOST': 'localhost',
        'PORT': 3306,
    }
}

