#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import RedirectView

admin.autodiscover()


urlpatterns = patterns('',
	url(r'^$', RedirectView.as_view(url= '/mobile/')),
	url(r'^hi/', include('hi.apps.mobile.urls', app_name='hi'), name='hi'),

	url(r'^grappelli/', include('grappelli.urls')),

    url(r'^admin/', include(admin.site.urls)),
)