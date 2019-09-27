"""Api URLs."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# View sets
from .views import cinco_de_oro as cinco_de_oro_viewset

# FCM router
routerCindoDeOro = DefaultRouter()
routerCindoDeOro.register(
	r'cincodeoro', cinco_de_oro_viewset.CincoDeOroViewSet, basename='cincodeoro')


urlpatterns = [
	path('', include('rest_auth.urls')),
	path('', include(routerCindoDeOro.urls)),  # Cinco de oro
]