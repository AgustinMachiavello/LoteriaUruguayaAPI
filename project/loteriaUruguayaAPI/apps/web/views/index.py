# Django views
from django.views.generic import TemplateView

# Django shortcuts
from django.shortcuts import render

from loteriaUruguayaAPI.settings.base import STATIC_URL


class IndexTemplateView(TemplateView):
	template_name = 'index.html'

	def get(self, request, *args, **kwargs):
		args = {'STATIC_URL': STATIC_URL}
		return render(request, self.template_name, args)
