import os

from .settings import *

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = ['morning-depths-38898.herokuapp.com']
