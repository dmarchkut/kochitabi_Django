import datetime
import json
from rest_framework import viewsets, filters
from collections import OrderedDict
from django.http.response import JsonResponse
from django.http import HttpResponse
from .models import Message, Coordinate, Photo_path, Spotimport datetime
from .views import render_json_response


def insert_temperature(request):
    data = json.loads(request.body.decode())
    coord = data['coord']
    coordinate = Coordinate.objects.all().filter(latitude=coord['lat']).filter(longitude=coord['lon']).first()
    if coordinate is None:
        #座標データが存在しない
        returnData = OrderedDict([
            ('update to Point_temperature', 'Not Find coordinate'),
            ('update to Environment', 'Do not execute'),
        ])
        return render_json_response(request, returnData)

    access_point = Access_point.objects.all().filter(coordinate_id=coordinate.coordinate_id).first()
    if access_point is None:
        #座標データが一致する観光地データが存在しない
        returnData = OrderedDict([
            ('update to Point_temperature', 'Not Find access_point'),
            ('update to Environment', 'Do not execute'),
        ])
        return render_json_response(request, returnData)

    point_temperature = Point_temperature.objects.all().filter(access_point_id=access_point.access_point_id).first()
    if point_temperature is None:
        #観光地データが一致する環境データが存在しない
        returnData = OrderedDict([
            ('update to Point_temperature', 'Not Find point_temperature'),
            ('update to Environment', 'Do not execute'),
        ])
        return render_json_response(request, returnData)

    mainData = data['main']
    temp = mainData['temp']
    point_temperature.point_temperature = temp
    point_temperature.update_at = str(datetime.datetime.now())
    point_temperature.save()

    #気温更新処理
    environment = Environment.objects.all().filter(spot_id=access_point.spot_id).first()
    if environment is None:
        #観光地データが一致する環境データが存在しない
        returnData = OrderedDict([
            ('update to Point_temperature', 'ok'),
            ('update to Environment', 'Not Find environment'),
        ])
        return render_json_response(request, returnData)
    print(environment.environment_id)
    point_temperature =  Point_temperature.objects.all().filter(environment_id=environment.environment_id).order_by('acquisition_rank').first()
    if point_temperature is None:
        #観光地データが一致する環境データが存在しない
        returnData = OrderedDict([
            ('update to Point_temperature', 'ok'),
            ('update to Environment', 'Not Find point_temperature'),
        ])
        return render_json_response(request, returnData)
    environment.temperature = point_temperature.point_temperature
    environment.update_at = str(datetime.datetime.now())
    environment.save()
    returnData = OrderedDict([
        ('update to Point_temperature', 'ok'),
        ('update to Environment', 'ok'),
    ])
    return render_json_response(request, returnData)
