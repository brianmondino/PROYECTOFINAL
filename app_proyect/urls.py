from django.urls import path
from app_proyect.views import products

urlpatterns = [
	path('', products, name = 'products'),
]