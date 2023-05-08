from .models import Url
from .serializers import UrlSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
import pyshorteners


@csrf_exempt
def url_list(request):
    """
    Get long urls by short_url.
    Create a new, short url.
    """

    if request.method == 'GET':
        if request.GET.get('short_url') is not None:
            short_url = request.GET.get('short_url')
            queryset = Url.objects.all().values('url', 'short_url', ).filter(short_url=short_url)
            data = list(queryset)
            return JsonResponse(data, safe=False)

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
