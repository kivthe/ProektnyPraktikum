"""
URL configuration for ProektnyPraktikum project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from api.views import CarlosonView, RentrideView, IndexView

urlpatterns = [
    path('admin/', admin.site.urls,name="admin"),
    path('api/', include('api.urls'),name="api"),
    path('home/',IndexView.as_view(),name="home"),
    path('json_with_carloson',CarlosonView.as_view(),name="carloson"),
    path('json_with_rentride',RentrideView.as_view(),name="rentride")
    #path('json_with_carloson_lite',name="carloson_lite"),
    #path('json_with_rentride_lite',name="rentride_lite")
]
