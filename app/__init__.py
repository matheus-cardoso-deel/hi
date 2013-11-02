# -*- coding : utf8 -*-

from flask import Flask

hi = Flask(__name__)
hi.debug = True

from app import views