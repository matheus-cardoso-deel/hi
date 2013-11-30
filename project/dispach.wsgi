import os
import sys
import site

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('/home/wendell/.virtualenvs/hi_v2.0.0/lib/python2.6/site-package')

# Add the app's directory to the PYTHONPATH
sys.path.append('/var/www/hi2.ruicadete.com.br')
sys.path.append('/var/www/hi2.ruicadete.com.br/hi')

os.environ['DJANGO_SETTINGS_MODULE'] = 'hi.settings'

# Activate your virtual env
activate_env=os.path.expanduser('/home/wendell/.virtualenvs/hi_v2.0.0/bin/activate_this.py')
execfile(activate_env, dict(__file__=activate_env))

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()