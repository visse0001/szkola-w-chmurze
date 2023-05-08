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
def url_list(request, pk=None):
    """
    Create a new, short url.
    """

    if request.method == 'GET':
        url = Url.objects.get(pk=pk)
        serializer = UrlSerializer(url)
        return JsonResponse(serializer.data)

    if request.method == 'POST':
        data = JSONParser().parse(request)

        if 'url' in data:

            shortener = pyshorteners.Shortener()
            short_url = shortener.tinyurl.short(data['url'])

            data.update({"short_url": short_url})

            serializer = UrlSerializer(data=data)
            if serializer.is_valid():
                serializer.save()

                return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)

        if "short_url" in data:
            short_url = Url.objects.filter(short_url="https://tinyurl.com/2j5lbmkg")
            serializer = UrlSerializer(short_url)
            # return JsonResponse(serializer.data, safe=False)
            return JsonResponse(serializer.data, safe=False, many=True)
