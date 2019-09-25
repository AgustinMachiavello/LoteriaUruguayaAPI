# Django views
from django.views.generic import TemplateView

# Django shortcuts
from django.shortcuts import render


class PricingTemplateView(TemplateView):
	template_name = 'pricing.html'

	def get(self, request, *args, **kwargs):
		args = {}
		return render(request, self.template_name, args)