from django.urls import path
from . import views

urlpatterns = [
    path('shrt', views.url_list),
]
