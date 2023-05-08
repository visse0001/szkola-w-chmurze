from .models import Url
from .serializers import UrlSerializer

from rest_framework import viewsets


class UrlViewSets(viewsets.ModelViewSet):
    queryset = Url.objects.all()
    serializer_class = UrlSerializer
