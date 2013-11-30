#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.utils.http import urlquote
from django.utils.translation import ugettext_lazy as _

from hi.apps.mobile.views.generic import load_json, GenericView, paginate
from hi.apps.accounts.models import CustomUser

class Event(models.Model):
    sender = models.ForeignKey(CustomUser, related_name='customuser_sender')
    reciver = models.ForeignKey(CustomUser, related_name='customuser_reciver')
    created_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return _('event')
        
    class Meta:
    	app_label = 'mobile'
        verbose_name = _('event')
        verbose_name_plural = _('events')