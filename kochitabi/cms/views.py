from django.shortcuts import render
#import django_gets
from rest_framework import viewsets, filters
from drf_multiple_model.views import MultipleModelAPIView
#from django import Person
from django.db import models
#from django.db.models import Person
import datetime
from collections import OrderedDict
#from django.http import HttpResponse
from django.http.response import JsonResponse

from .models import Message, Coordinate, Photo_path, Spot, Character, Environment, Access_point, Character_data, Spot_photo
from .serializer import MessageSerializer, CoordinateSerializer, Photo_pathSerializer, SpotSerializer, CharacterSerializer, EnvironmentSerializer, Access_pointSerializer, Character_dataSerializer

"""
class Coordinate(models.Model):
    coordinate_id   = models.CharField('座標ID', primary_key=True, max_length = 6, null=False)
    place_name      = models.TextField('地名', max_length = 50, null=False)
    latitude        = models.FloatField('緯度', max_length = 10, null = False)
    longitude       = models.FloatField('経度', max_length = 11, null=False)
    created_at      = models.DateTimeField('作成日時', null=False)
    update_at       = models.DateTimeField('更新日時', null=False)
    def __str__(self):
        return self.coordinate_id


class local_spots(models.Model):
    spot_id
    environment_id
    spot_name
    spot_phoname
    street_address
    postal_code
    latitude
    longitude
    photo_file_path
    text_data
    created_at
    update_at

Book.objects.values_list('title', flat=True)
[u'Clean Corder',  u'アジャイルサムライ', u'ハッカーと画家']
"""







#class Local_spotViewSet(viewsets.ModelViewSet):
#f_artist_tmp = FestivalArtistTagTmp.objects.all().filter(tag_name=artist_string).first()
def Local_spotViewSet(request):
    local_spots = []
    #spot_ids = Spot.objects.values_list('spot_id', flat=True)
    for spot in Spot.objects.all().order_by('spot_id'):
        #特定のレコードを呼び出すためのキーを取得
        coordinate_id = spot.coordinate_id
        message_id = spot.message_id
        #use_photo_path_id = Spot_photo.objects.all().filter(spot_id=spot.spot_id).first().use_photo_path_id

        #テーブルよりレコードを取得
        coordinate = Coordinate.objects.all().filter(coordinate_id=coordinate_id).first()
        message = Message.objects.all().filter(message_id=message_id).first()
        environment = Environment.objects.all().filter(spot_id=spot.spot_id).first()
        #photo_path = Photo_path.objects.all().filter(photo_path_id=use_photo_path_id).first()
        spot_photo = Spot_photo.objects.all().filter(spot_id=spot.spot_id).first()
        print(spot_photo.use_photo_path_id)
        photo_path = Photo_path.objects.all().filter(photo_path_id=spot_photo.use_photo_path_id).first()

        local_spot = OrderedDict([
            #('id', impression.id)
            ('spot_id', spot.spot_id),
            ('environment_id', environment.environment_id),
            ('spot_phoname', spot.spot_phoname),
            ('street_address', spot.steet_address),
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







"""
    queryset = []
    spot_ids = Spot.objects.values_list('spot_id', flat=True)
    for spot_id in spot_ids:
        coordinate_id = Spot.objects.values_list('coordinate_id', flat=True).filter(spot_id=spot_id)
        message_id = Spot.objects.values_list('message_id', flat=True).filter(spot_id=spot_id)
        use_photo_path_id = Spot_photo.objects.values_list('use_photo_path_id', flat=True).filter(spot_id=spot_id)

        queryset.extend({
            "spot_id" : spot_id,
            "environment_id" : "%s" % Environment.objects.values_list('environment_id', flat=True).filter(spot_id=spot_id),
            "spot_phoname" : "%s" % Spot.objects.values_list('spot_phoname', flat=True).filter(spot_id=spot_id),
            "street_address" : "%s" % Spot.objects.values_list('steet_address', flat=True).filter(spot_id=spot_id),
            "postal_code" : "%s" % Spot.objects.values_list('postal_code', flat=True).filter(spot_id=spot_id),
            "latitude" : "%s" % Coordinate.objects.values_list('latitude', flat=True).filter(coordinate_id=coordinate_id),
            "longitude" : "%s" % Coordinate.objects.values_list('longitude', flat=True).filter(coordinate_id=coordinate_id),
            "photo_file_path" : "%s" % Photo_path.objects.values_list('photo_file_path', flat=True).filter(photo_path_id=use_photo_path_id),
            "text_data" : "%s" % Message.objects.filter(message_id=message_id).values_list('text_data', flat=True),
            "created_at" : "%s" % datetime.datetime.now(),
            "update_at" : "%s" % datetime.datetime.now()
        })
"""
"""
        queryset.entry_set.create(
            spot_id,
            environment_id  = Environment.objects.values_list('environment_id', flat=True).filter(spot_id=spot_id),
            spot_phoname    = Spot.objects.values_list('spot_phoname', flat=True).filter(spot_id=spot_id),
            street_address  = Spot.objects.filter(spot_id=spot_id).values_list('street_address', flat=True),
            postal_code     = Spot.objects.filter(spot_id=spot_id).values_list('postal_code', flat=True),
            latitude        = Coordinate.objects.filter(spot_id=coordinate_id).values_list('latitude', flat=True),
            longitude       = Coordinate.objects.filter(spot_id=coordinate_id).values_list('longitude', flat=True),
            photo_file_path = Photo_path.objects.filter(spot_id=use_photo_path_id).values_list('photo_file_path', flat=True),
            text_data       = Message.objects.filter(message_id=message_id).values_list('text_data', flat=True),
            created_at      = datetime.datetime.now(),
            update_at       = datetime.datetime.now()
        )
"""




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
