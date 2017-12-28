import datetime
from rest_framework import viewsets, filters
from collections import OrderedDict
from django.http.response import JsonResponse
from .models import Message, Coordinate, Photo_path, Spot, Character, Environment, Access_point, Character_data, Spot_photo
from .serializer import MessageSerializer, CoordinateSerializer, Photo_pathSerializer, SpotSerializer, CharacterSerializer, EnvironmentSerializer, Access_pointSerializer, Character_dataSerializer

def Local_spotViewSet(request):
    local_spots = []

    for spot in Spot.objects.all().order_by('spot_id'):

        #特定のレコードを呼び出すためのキーを取得
        coordinate_id = spot.coordinate_id
        message_id = spot.message_id
        #テーブルよりレコードを取得
        coordinate = Coordinate.objects.all().filter(coordinate_id=coordinate_id).first()
        message = Message.objects.all().filter(message_id=message_id).first()
        environment = Environment.objects.all().filter(spot_id=spot.spot_id).first()
        spot_photo = Spot_photo.objects.all().filter(spot_id=spot.spot_id).first()
        photo_path = Photo_path.objects.all().filter(photo_path_id=spot_photo.use_photo_path_id).first()

        local_spot = OrderedDict([
            ('spot_id', spot.spot_id),
            ('environment_id', environment.environment_id),
            ('spot_phoname', spot.spot_phoname),
            ('street_address', spot.street_address),
            ('postal_code', spot.postal_code),
            ('latitude', coordinate.latitude),
            ('longitude', coordinate.longitude),
            ('photo_file_path', photo_path.photo_file_path),
            ('text_data', message.text_data),
            ('created_at', datetime.datetime.now()),
            ('update_at', datetime.datetime.now()),
        ])
        local_spots.append(local_spot)

    data = OrderedDict([ ('local_spot', local_spot) ])
    return JsonResponse(data)


def Local_environment(request):
    local_environments = []

    for environment in Environment.objects.all().order_by('environment_id'):

        environment = OrderedDict([
            ('environment_id', environment.environment_id),
            ('weather', environment.weather),
            ('temperature', environment.temperature),
            ('created_at', datetime.datetime.now()),
            ('update_at', datetime.datetime.now()),
        ])
        local_environments.append(environment)

    data = OrderedDict([ ('local_spot', local_environments)])
    return JsonResponse(data)


def Local_access_point(request):
    local_access_points = []

    for access_point in Access_point.objects.all().order_by('access_point_id'):

        coordinate_id = access_point.coordinate_id
        message_id = access_point.message_id
        spot_id = access_point.spot_id
        spot = Spot.objects.all().filter(spot_id=spot_id).first()
        coordinate = Coordinate.objects.all().filter(coordinate_id=coordinate_id).first()
        message = Message.objects.all().filter(message_id=message_id).first()

        local_access_point = OrderedDict([
            ('access_point_id', access_point.access_point_id),
            ('spot_id', spot.spot_id),
            ('access_point_name', access_point.access_point_name),
            ('latitude', coordinate.latitude),
            ('longitude', coordinate.longitude),
            ('text_data', message.text_data),
            ('created_at', datetime.datetime.now()),
            ('update_at', datetime.datetime.now()),
        ])
        local_access_points.append(local_access_point)

    data = OrderedDict([('local_access_point', local_access_points)])
    return JsonResponse(data)


def Local_character(request):
    local_characters = []

    for character_data in Character_data.objects.all().order_by('character_data_id'):
        character_id = character_data.character_id
        access_point_id = character_data.access_point_id
        character = Character.objects.all().filter(character_id=character_id).first()
        access_point = Access_point.objects.all().filter(access_point_id=access_point_id).first()

        local_character = OrderedDict([
            ('access_point_id', access_point.access_point_id),
            ('character_name', character.character_name),
            ('character_file_path', character_data.character_file_pass),
            ('created_at', datetime.datetime.now()),
            ('update_at', datetime.datetime.now()),
        ])
        local_characters.append(local_character)

    data = OrderedDict([('local_character', local_characters)])
    return JsonResponse(data)



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
