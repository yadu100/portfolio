from django.contrib import admin
from django.urls import path,include

from . import views

urlpatterns = [
    path('', views.ProjectPage, name='project'),
    path('<str:pk>/', views.SingleProjectPage, name='singleproject'),
]