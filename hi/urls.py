#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import RedirectView

admin.autodiscover()


urlpatterns = patterns('',
	url(r'^$', RedirectView.as_view(url='/accounts/logon/')),
	url(r'^mobile/', include('hi.apps.mobile.urls', app_name='mobile'), name='mobile'),
	url(r'^accounts/', include('hi.apps.accounts.urls', app_name='accounts'), name='accounts'),


	url(r'^grappelli/', include('grappelli.urls')),

    url(r'^admin/', include(admin.site.urls)),
)