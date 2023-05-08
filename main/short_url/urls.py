from rest_framework import routers
from django.urls import path, include
from .views import UrlViewSets

router = routers.DefaultRouter()
router.register(r'shrt', UrlViewSets)

urlpatterns = [
    path('api/', include(router.urls)),
]
