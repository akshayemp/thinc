# coding: utf-8
from __future__ import unicode_literals

from os import path, environ


PWD = path.join(path.dirname(__file__), '..')
ENV = environ["VENV_DIR"] if 'VENV_DIR' in environ else '.env'
VENV_DIR = path.join(PWD, ENV)
