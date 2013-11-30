#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from __future__ import unicode_literals
import re

from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, BaseUserManager, UserManager)
from django.core.mail import send_mail
from django.core import validators
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

# from hi.apps.mobile.models.position import Position

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        _('username'), 
        max_length=30, 
        unique=True,
        help_text=_('Required. 30 characters or fewer. Letters, numbers and @/./+/-/_ characters'),
        validators=[
            validators.RegexValidator(re.compile('^[\w.@+-]+$'), _('Enter a valid username.'), 'invalid')
        ]
    )
    email = models.EmailField(
        _('email address'), 
        max_length=254, 
        unique=True,
        help_text=_('User email.'),
    )
    first_name = models.CharField(
        _('first name'), 
        max_length=254, 
        blank=True,
        help_text=_('User first name.'),        

    )
    last_name = models.CharField(
        _('last name'), 
        max_length=30, 
        blank=True,
        help_text=_('User last name.'),        
    )
    description = models.CharField(
        _('description'), 
        max_length=500, 
        blank=True,
        help_text=_('User description.'),        
    )
    # position = models.ForeignKey(
    #     Position
    # )
    is_staff = models.BooleanField(
        _('staff status'), 
        default=True,
        help_text=_('Designates whether the user can log into this admin site.')
    )
    is_active = models.BooleanField(
        _('active'), 
        default=True,
        help_text=_('Designates whether this user should be treated as active. Unselect this instead of deleting accounts.')
    )
    date_joined = models.DateTimeField(
        _('date joined'), 
        default=timezone.now
    )

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [
        'email',
    ]

    class Meta:
        verbose_name = _('user') 
        verbose_name_plural = _('users') 

    def __unicode__(self):

        return self.username

    def get_first_name(self):

        first_name = self.first_name
        return first_name.strip()

    def get_last_name(self): 

        return self.last_name.strip()

    def email_user(self, subject, message, from_email=None): 

        send_mail(subject, message, from_email, [self.email])
