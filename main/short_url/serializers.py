from rest_framework import serializers
from .models import Url


class UrlSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Url
        fields = ['id', 'created', 'url', 'short_url']
