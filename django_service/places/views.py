from rest_framework.response import Response
from rest_framework.views import APIView
from places.models import Place
from .serializer import PlaceSerializer

class PlaceListApi(APIView):
    def get(self, request):
        places = Place.objects.all()
        serializer = PlaceSerializer(places, many=True)
        return Response({'places': serializer.data})