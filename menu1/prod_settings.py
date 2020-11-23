import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = '233443jknjkn34iggngk4v(2b*9atbz&fe_zl$-0zv0-1kwu2s1ao*bhaxldhqn7'

DEBUG = True

ALLOWED_HOSTS = ["185.154.14.236"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ecomenu',
        'USER': 'momyn',
        'PASSWORD': '87475643797m',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}



STATIC_ROOT = str(BASE_DIR.joinpath('staticfiles'))
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    '/var/www/static/',
)
