import pathlib

BASE_DIR = pathlib.Path(__file__).resolve().parent

DEBUG = False

ALLOWED_HOSTS = ['benjah.pythonanywhere.com']

STATIC_ROOT = BASE_DIR / 'staticfiles'

ROOT_URLCONF = 'benmwasya.urls'