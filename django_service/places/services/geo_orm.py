from django.contrib.gis.geos import Point
from django.http import JsonResponse
from places.models import Place
from django.contrib.gis.db import models

def near_place(lat, lon, count=5):
    try:
        lat = float(lat)
        lon = float(lon)
        user_location = Point(lon, lat, srid=4326)  # Создаем точку для пользователя

        # Находим ближайшие 5 мест
        places = Place.objects.annotate(
            distance=models.functions.Distance('location', user_location)
        ).order_by('distance')[:5]

        # Формируем ответ
        result = [
            {
                'name': place.name,
                'coordinates': {
                    'latitude': place.location.y,
                    'longitude': place.location.x
                },
                'distance_km': round(place.distance.km, 2)  # Расстояние в километрах
            }
            for place in places
        ]

        return JsonResponse({'places': result}, status=200)

    except ValueError:
        return JsonResponse({'error': 'Invalid coordinates'}, status=400)