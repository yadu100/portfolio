from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.ArticlesPage, name='articles'),
    path('<str:pk>/', views.SingleArticlePage, name='singlearticle'),
]