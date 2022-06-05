from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from app_proyect.models import Products

def products(request):
        productos = Products.objects.all()
        context = {'productos':productos}
        return render(request, 'products.html', context=context)

def create_product(request):
	return render(request, 'create_product.html')