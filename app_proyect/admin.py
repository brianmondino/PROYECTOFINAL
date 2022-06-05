from django.contrib import admin

from app_proyect.models import Products

# Register your models here.
admin.site.register(Products)       #para registrar producots desde la pag de admin. dice (Products) porque asi se llama la class en models.py