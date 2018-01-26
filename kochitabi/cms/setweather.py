import datetime
import json
from rest_framework import viewsets, filters
from collections import OrderedDict
from django.http.response import JsonResponse
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from .models import Message, Coordinate, Photo_path, Spot, Character, Environment, Access_point, Character_data, Spot_photo
from .views import render_json_response


@require_http_methods(["POST"])
def insert_weathers(request):
    data = json.loads(request.body.decode())
    coord = data['coord']
    coordinate = Coordinate.objects.all().filter(latitude=coord['lat']).filter(longitude=coord['lon']).first()
    if coordinate is None:
        #座標データが存在しない
        returnData = OrderedDict([
            ('update to Environment', 'Not Find point_temperature'),
        ])
        return render_json_response(request, returnData)

    spot = Spot.objects.all().filter(coordinate_id=coordinate.coordinate_id).first()
    if spot is None:
        #座標データが一致する観光地データが存在しない
        returnData = OrderedDict([
            ('update to Environment', 'Not Find spot'),
        ])
        return render_json_response(request, returnData)

    environment = Environment.objects.all().filter(spot_id=spot.spot_id).first()
    if environment is None:
        #観光地データが一致する環境データが存在しない
        returnData = OrderedDict([
            ('update to Environment', 'Not Find environment'),
        ])
        return render_json_response(request, returnData)

    weather = data['weather']
    weather = weather[0]
    weather_main = weather['main']

    if weather_main == "Thunderstorm":
        weatherText = "雷雲"
    elif weather_main == "Drizzle":
        weatherText = "霧雨"
    elif weather_main == "Rain":
        weatherText = "雨"
    elif weather_main == "Snow":
        weatherText = "雪"
    elif weather_main == "Atmosphere":
        weatherText = "霧"
    elif weather_main == "Clear":
        weatherText = "晴れ"
    elif weather_main == "Clouds":
        weatherText = "曇り"
    else:
        weatherText = "その他"

    environment.weather = weatherText
    environment.update_at = str(datetime.datetime.now())
    environment.save()

    returnData = OrderedDict([
        ('update to Environment', 'ok'),
    ])
    return render_json_response(request, returnData)
