# -*- coding: utf-8 -*-

# Django Imports
from django.urls import path

# Project Imports
from . import views


urlpatterns = [

    path('', views.home, name='home'),
    path('using-celery/', views.mail_using_celery, name='using_celery'),
    path('without-celery/', views.mail_without_celery, name='without_celery'),
]