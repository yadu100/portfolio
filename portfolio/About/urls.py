from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.AboutPage, name='About'),
    path('contact/', views.ContactPage, name='contact'),
]