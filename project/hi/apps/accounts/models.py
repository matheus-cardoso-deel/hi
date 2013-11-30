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
from hi.apps.management.models import Role, Business

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
    full_name = models.CharField(
        _('full name'), 
        max_length=254, 
        blank=True,
        help_text=_('User full name.'),        

    )
    short_name = models.CharField(
        _('short name'), 
        max_length=30, 
        blank=True,
        help_text=_('User short name.'),        
    )
    email = models.EmailField(
        _('email address'), 
        max_length=254, 
        unique=True,
        help_text=_('User email.'),
    )
    cpf = models.CharField(
        _('cpf'),
        max_length=11,
        null=False,
        help_text=_('User CPF.'),
    )
    role = models.ForeignKey(
        Role,
        null=True,
        help_text=_('User role.'),
    )
    businesses = models.ManyToManyField(
        Business,
        help_text=_('User businesses.')
    )
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
        'cpf', 
        'email',
    ]

    class Meta:
        verbose_name = 'colaborador' # Translation not found to 'colaborador'
        verbose_name_plural = 'colaboradores' # Translation not found to 'colaboradores'

    def __unicode__(self):

        return self.username

    def get_full_name(self):

        full_name = self.full_name
        return full_name.strip()

    def get_short_name(self): 

        return self.short_name.strip()

    def email_user(self, subject, message, from_email=None): 

        send_mail(subject, message, from_email, [self.email])

class CollaboratorUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        _('username'), 
        max_length=30, 
        unique=True,
        help_text=_('Required. 30 characters or fewer. Letters, numbers and @/./+/-/_ characters'),
        validators=[
            validators.RegexValidator(re.compile('^[\w.@+-]+$'), _('Enter a valid username.'), 'invalid')
        ]
    )
    full_name = models.CharField(
        _('full name'), 
        max_length=254, 
        blank=True,
        help_text=_('Collaborator full name.'),        

    )
    short_name = models.CharField(
        _('short name'), 
        max_length=30, 
        blank=True,
        help_text=_('Collaborator short name.'),        
    )
    email = models.EmailField(
        _('email address'), 
        max_length=254, 
        unique=True,
        help_text=_('Collaborator email.'),
    )
    cpf = models.CharField(
        _('cpf'),
        max_length=11,
        null=False,
        help_text=_('Collaborator CPF.'),
    )
    role = models.ForeignKey(
        Role,
        null=True,
        help_text=_('Collaborator role.'),
    )
    businesses = models.ManyToManyField(
        Business,
        help_text=_('Collaborator businesses.')
    )
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
        'cpf', 
        'email',
    ]

    class Meta:
        verbose_name = 'colaborador' # Translation not found to 'colaborador'
        verbose_name_plural = 'colaboradores' # Translation not found to 'colaboradores'

    def __unicode__(self):

        return self.username

    def get_full_name(self):

        full_name = self.full_name
        return full_name.strip()

    def get_short_name(self): 

        return self.short_name.strip()

    def email_user(self, subject, message, from_email=None): 

        send_mail(subject, message, from_email, [self.email])