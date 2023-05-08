from .models import Url
from .serializers import UrlSerializer
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
import pyshorteners


@csrf_exempt
def url_list(request):
    """
    Create a new, short url.
    """

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UrlSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

            shortener = pyshorteners.Shortener()
            short_url = shortener.tinyurl.short(data['url'])

            response = serializer.data
            response.update({'short_url': short_url})

            return JsonResponse(response, status=201)
        return JsonResponse(serializer.errors, status=400)
