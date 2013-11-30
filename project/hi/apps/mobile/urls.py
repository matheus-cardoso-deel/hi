#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic.base import RedirectView

from views import *

urlpatterns = patterns('',
	url(r'^$', 'hi.apps.mobile.views.generic.logon', name='logon',),
	
	url(r'^logon', 'hi.apps.mobile.views.generic.logon', name='logon',),
	url(r'^logoff', 'hi.apps.mobile.views.generic.logoff', name='logoff',),
	
	url(r'^home', 'hi.apps.mobile.views.generic.home', name='home',),
	url(r'^register', 'hi.apps.mobile.views.generic.register', name='register',),

	# home
	# url(r'^home/(?P<slug>\w+)/$', login_required(home.HomeView.as_view()), name='home',),
	# url(r'^home/(?P<slug>\w+)/(?P<key>\d+)/$', login_required(home.HomeView.as_view()), name='home',),
)