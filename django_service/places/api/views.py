from rest_framework.response import Response
from rest_framework.views import APIView
from places.models import Place
from .serializers import PlaceSerializer
from django.http import JsonResponse

from ..services.geo_orm import near_place


class PlaceListApi(APIView):
    def get(self, request):
        places = Place.objects.all()
        serializer = PlaceSerializer(places, many=True)
        return Response({'places': serializer.data})


class NearPlace(APIView):
    def get(self, request, *args, **kwargs):
        lat = request.GET.get('lat')
        lon = request.GET.get('lon')
        count = request.GET.get('count')
        print(lat, lon, count)

        if lat and lon:
            answer = near_place(lat, lon, count)
            return answer

        return JsonResponse({'error': 'Coordinates not provided'}, status=400)