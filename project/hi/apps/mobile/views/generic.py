#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from django.template.loader import render_to_string

from django.views.generic import View

#
# Dumps and loads JSON
#

def render_to_json(request, template, context_data):
	response = {}	

	try: 
		return context_data['file']
	except:
		pass
	
	try:
		template_data = context_data['template']
	except:
		template_data = None
		
	try:
		response['template'] = render_to_string(template, template_data, context_instance=RequestContext(request))
	except:
		pass
		
	try:
		for key, value in context_data['leftover'].items():	
			response[key] = value
	except:
		pass

	return HttpResponse(json.dumps(response), mimetype='application/json')

def load_json(request):

	try:
		response = json.loads(request)
	except:
		response = None

	return response

#
# Generic View
#

class GenericView(View):
	def post(self, request, *args, **kwargs):

		if request.is_ajax():

			return render_to_json(request, self.get_template_name(request), self.get_context_data(request))
		else:
			context_data = self.get_context_data(request)

			try:
				template_data = context_data['template']
			except:
				template_data = None
				
			try:
				return context_data['file']
			except:
				return render_to_response(self.get_template_name(request), template_data, context_instance=RequestContext(request))
		
	def get(self, request, *args, **kwargs):

		if request.is_ajax():

			return render_to_json(request, self.get_template_name(request), self.get_context_data(request))
		else:
			context_data = self.get_context_data(request)

			try:
				template_data = context_data['template']
			except:
				template_data = None				

			try:
				return context_data['file']
			except:
				return render_to_response(self.get_template_name(request), template_data, context_instance=RequestContext(request))

	def get_template_name(self, request):
		page_name = request.resolver_match.url_name

		if request.is_ajax():

			path = 'mobile/' + page_name + '/'
		else:
			path = 'mobile/' + page_name + '/nonajax/'

		try:
			slug = str(self.kwargs['slug'])

			path = path + slug + '.html'

			print path
			try:
				template = loader.get_template(path)

				return path
			except:
				return 'mobile/404.html'
		except:
			return 'mobile/404.html'

#
# Paginate
#

def paginate(obj, page, num_per_page):
	paginator = Paginator(obj, num_per_page)

	try:
		page = int(page)
		obj = paginator.page(page)
	except PageNotAnInteger:
		page = 1
		obj = paginator.page(page)
	except EmptyPage:
		page = paginator.num_pages
		obj = paginator.page(page)
	except:
		page = 1
		obj = paginator.page(page)

	try:
		paginator.page(page - 10)
		paginator.page(page - 11)

		obj.has_less_ten = page - 10					
	except EmptyPage:
		pass

	try:
		paginator.page(page - 2)
		obj.has_less_two = page - 2
	except EmptyPage:
		pass

	try:
		paginator.page(page - 3)
		obj.has_less_three = page - 3
	except EmptyPage:
		pass

	obj.page = page

	try:
		paginator.page(page + 2)
		obj.has_more_two = page + 2
	except EmptyPage:
		pass

	try:
		paginator.page(page + 3)
		obj.has_more_three = page + 3
	except EmptyPage:
		pass
	
	try:
		paginator.page(page + 10)
		paginator.page(page + 11)

		obj.has_more_ten = page + 10					
	except EmptyPage:
		pass

	return obj

#
# Default pages
#

def logon(request):

	if request.user.is_authenticated():
		return HttpResponseRedirect('/mobile/index/')
	elif request.POST: 
		if 'username' in request.POST and request.POST['username']:
			username = request.POST['username']
		if 'password' in request.POST and request.POST['password']:
			password = request.POST['password']

		if username != None and password != None:
			authenticated_user = authenticate(username=username, password=password)

			if authenticated_user is not None:
				if authenticated_user.is_active:
					login(request, authenticated_user)

					return index(request)
				else:
					return initial(request)
			else:
				return initial(request)
		else:
			return initial(request)
	else:   
		return HttpResponseRedirect('mobile/logon.html')

def logoff(request):
    logout(request)

    return HttpResponseRedirect('/mobile/')