"""prototype URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from .views import render_template
from django.views.generic.base import RedirectView
from django.urls import path
from cantonsdistricts import views

urlpatterns = [
  #  path('/index.html', views.IndexView.as_view(), name='index'),
  #  url(r'^$', RedirectView.as_view(url='/index.html')),
  #  url(r'^(?P<template>.+)$',render_template), # cualquier cosa se renderiza con template
  #  url(r'^admin/', admin.site.urls),
 #   url(r'^index/', views.Index),
 #   path('articles/2003/', views.special_case_2003),
   # url(r'^cantons/',Lista, name='cantons')
    path('',views.Index,name='index')
]
