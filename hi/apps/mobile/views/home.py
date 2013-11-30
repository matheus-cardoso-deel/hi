#!/usr/bin/env python
# -*- coding: utf-8 -*-

from hi.apps.management.models import *
from hi.apps.mobile.views.generic import load_json, GenericView

class HomeView(GenericView):
					
	def get_context_data(self, request):

		try:
			slug = self.kwargs['slug']	
		except:
			return None