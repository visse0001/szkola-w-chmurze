from rest_framework import serializers
from .models import Url

import pyshorteners


class UrlSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Url
        fields = ['id', 'created', 'url', 'short_url']
