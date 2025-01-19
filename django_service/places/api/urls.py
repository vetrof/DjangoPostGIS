
from django.contrib import admin
from django.urls import path, include

from .views import PlaceListApi, NearPlace, PlaceDetail

urlpatterns = [
    path('all/', PlaceListApi.as_view()),
    path('near/', NearPlace.as_view()),
    path('detail/<int:id>/', PlaceDetail.as_view()),
]
