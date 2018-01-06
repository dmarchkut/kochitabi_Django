import datetime
import json
from rest_framework import viewsets, filters
from collections import OrderedDict
from django.http.response import JsonResponse
from django.http import HttpResponse
from .models import Message, Coordinate, Photo_path, Spot, Character, Environment, Access_point, Character_data, Spot_photo, Point_temperature
from .views import render_json_response


def insert_temperature(request):
    data = json.loads(request.body.decode())
    coord = data['coord']
    coordinate = Coordinate.objects.all().filter(latitude=coord['lat']).filter(longitude=coord['lon']).first()
    if coordinate is None:
        #座標データが存在しない
        return

    access_point = Access_point.objects.all().filter(coordinate_id=coordinate.coordinate_id).first()
    if access_point is None:
        #座標データが一致する観光地データが存在しない
        return

    point_temperature = Point_temperature.objects.all().filter(access_point_id=access_point.access_point_id).first()
    if point_temperature is None:
        #観光地データが一致する環境データが存在しない
        return

    mainData = data['main']
    temp = mainData['temp']
    point_temperature.point_temperature = temp
    point_temperature.save()

    returnData = OrderedDict([
        ('temperature', temp),
    ])
    return render_json_response(request, returnData)
