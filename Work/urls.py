from django.contrib import admin
from django.urls import path,include

from . import views

urlpatterns = [
    path('', views.WorkPage, name='work'),
    path('<str:pk>/',views.SingleWorkPage, name='singlework'),
]