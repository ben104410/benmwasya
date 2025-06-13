import pathlib

BASE_DIR = pathlib.Path(__file__).resolve().parent

DEBUG = False

ALLOWED_HOSTS = ['yourusername.pythonanywhere.com']

STATIC_ROOT = BASE_DIR / 'staticfiles'