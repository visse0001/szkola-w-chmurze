from django.urls import path
from . import views

urlpatterns = [
    path('shrt', views.url_list),
    # path('shrt/<short_url>/', views.url_list),
]
