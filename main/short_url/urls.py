from django.urls import path
from . import views

urlpatterns = [
    path('shrt', views.url_list),
    path('shrt/<int:pk>/', views.url_list),
]
