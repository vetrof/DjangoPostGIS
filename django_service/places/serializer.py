from rest_framework import serializers
from django.contrib.gis.geos import Point
from places.models import Place

class PlaceSerializer(serializers.ModelSerializer):
    # Преобразуем поле location в строку (широта, долгота)
    location = serializers.SerializerMethodField()

    class Meta:
        model = Place
        fields = ['name', 'location']

    def get_location(self, obj):
        if obj.location:
            # Возвращаем строку в формате "longitude, latitude"
            return f"{obj.location.x}, {obj.location.y}"
        return None