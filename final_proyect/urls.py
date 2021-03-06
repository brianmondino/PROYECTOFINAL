"""final_proyect URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from final_proyect.views import welcome, index


urlpatterns = [
    path('', index, name = 'index'),                    #ACA '' ESTA ASI PORQUE ES EL INDEX

    path('admin/', admin.site.urls),                    # acá es url , el sitio de admin
    path('welcome/', welcome, name = 'welcome'),        # acá es url , redigire a welcome (una funcion que esta en views.py), nombre que aparece en la url

    path('products/', include('app_proyect.urls')),     #acá redirecciona a urls de app_proyect donde existe products
]

