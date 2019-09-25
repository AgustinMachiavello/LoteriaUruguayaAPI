from django.contrib import admin
from django.urls import path, include

# Django REST Framework
from rest_framework.authtoken import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

# Views
from .views import (
	index,
	pricing,
)

urlpatterns = [
    path('', index.IndexTemplateView.as_view(), name='index'),
	path('pricing/', pricing.PricingTemplateView.as_view(), name='pricing'),
    path('admin/', admin.site.urls),

]