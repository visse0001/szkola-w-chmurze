from rest_framework import routers
from django.urls import path, include
from . import views

urlpatterns = [
    path('shrt', views.url_list),
    path('shrt/<int:pk>/', views.url_list),
]
