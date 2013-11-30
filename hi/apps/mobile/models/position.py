#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.utils.http import urlquote
from django.utils.translation import ugettext_lazy as _


from hi.apps.mobile.views.generic import load_json, GenericView, paginate

class Position(models.Model):
    latitude = models.FloatField(_('latitude'), null=False, help_text=_('User latitude.'))
    longitude = models.FloatField(_('longitude'), null=False, help_text=_('User longidute.'))

    def __unicode__(self):
        return _('position')
        
    class Meta:
    	app_label = 'mobile'
        verbose_name = _('position')
        verbose_name_plural = _('positions')