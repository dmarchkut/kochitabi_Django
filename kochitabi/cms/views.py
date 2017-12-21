from django.shortcuts import render
import django_filters
from rest_framework import viewsets, filters

from .models import Message, Coordinate, Photo_path, Spot, Character, Environment, Access_point, Character_data
from .serializer import MessageSerializer, CoordinateSerializer, Photo_pathSerializer, SpotSerializer, CharacterSerializer, EnvironmentSerializer, Access_pointSerializer, Character_dataSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class CoordinateViewSet(viewsets.ModelViewSet):
    queryset = Coordinate.objects.all()
    serializer_class = CoordinateSerializer


class Photo_pathViewSet(viewsets.ModelViewSet):
    queryset = Photo_path.objects.all()
    serializer_class = Photo_pathSerializer


class SpotViewSet(viewsets.ModelViewSet):
    queryset = Spot.objects.all()
    serializer_class = SpotSerializer


class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer


class EnvironmentViewSet(viewsets.ModelViewSet):
    queryset = Environment.objects.all()
    serializer_class = EnvironmentSerializer


class Access_pointViewSet(viewsets.ModelViewSet):
    queryset = Access_point.objects.all()
    serializer_class = Access_pointSerializer


class Character_dataViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
