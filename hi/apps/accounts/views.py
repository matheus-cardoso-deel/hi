#!/usr/bin/env python
# -*- coding: utf-8 -*-

from hi.apps.mobile.views.generic import load_json, GenericView
from hi.apps.accounts.models import CustomUser

class AccountsView(GenericView):
					
	def get_context_data(self, request):

		try:
			slug = self.kwargs['slug']	

			if slug == 'create':
				if request.POST:
					try:
						username = request.POST['username']
						password1 = request.POST['password1']
						password2 = request.POST['password2']
						first_name = request.POST['first_name']
						last_name = request.POST['last_name']
						email = request.POST['email']

						return CustomUser.create_basic_user(
							username=username,
							password1=password1,
							password2=password2,
							email=email,
							first_name=first_name,
							last_name=last_name,
						)

					except:
						return {'leftover' : {
								'alert-error' : 'Todas as informações são necessárias para efetuar o cadastro.',
							}
						}
				elif request.GET:

					return None
			elif slug == 'logon':
				if request.POST:
					try:
						username = request.POST['username']
						password = request.POST['password']

						if username == '' or password == '':
							return {'leftover' : {
									'alert-error' : 'Todas as informações são necessárias para entrar no sistema.',
								}
							}
						else:	
							return CustomUser.logon(
								request=request,
								username=username, 
								password=password,
							)

					except:
						return {'leftover' : {
								'alert-error' : 'Todas as informações são necessárias para entrar no sistema.',
							}
						}	
				elif request.GET:

					return None
			elif slug == 'logoff':
				    logout(request)

    			return HttpResponseRedirect('/mobile/')

		except:
			return None