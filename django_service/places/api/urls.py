
from django.contrib import admin
from django.urls import path, include

from .views import PlaceListApi, NearPlace

urlpatterns = [
    path('all/', PlaceListApi.as_view()),
    path('near/', NearPlace.as_view()),
]
