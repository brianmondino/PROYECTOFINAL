from django.urls import path
from app_proyect.views import products, create_product

urlpatterns = [
	path('', products, name = 'products'),
	path('create-product/', create_product, name ='create_product'),
]