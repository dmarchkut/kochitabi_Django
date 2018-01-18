import datetime
import json
from collections import OrderedDict
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from cms.models import (Message, Coordinate, Photo_path, Spot, Character,
                        Environment, Access_point, Character_data, Spot_photo)


def render_json_response(request, data, status=None):
    """response を JSON で返却"""
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    callback = request.GET.get('callback')
    if not callback:
        callback = request.POST.get('callback')
    if callback:
        json_str = "%s(%s)" % (callback, json_str)
        response = HttpResponse(json_str, content_type='application/javascript; charset=UTF-8', status=status)
    else:
        response = HttpResponse(json_str, content_type='application/json; charset=UTF-8', status=status)
    return response


@require_http_methods(["GET", "POST"])
def Local_spotViewSet(request):
    """ローカル観光地"""
    local_spots = []

    for spot in Spot.objects.all().order_by('spot_id'):

        #特定のレコードを呼び出すためのキーを取得
        coordinate_id = spot.coordinate_id
        message_id = spot.message_id
        #テーブルよりレコードを取得
        coordinate = Coordinate.objects.all().filter(coordinate_id=coordinate_id).first()
        message = Message.objects.all().filter(message_id=message_id).first()
        environment = Environment.objects.all().filter(spot_id=spot.spot_id).first()
        if environment is None:
            continue
        spot_photo = Spot_photo.objects.all().filter(spot_id=spot.spot_id).first()
        if spot_photo is None:
            continue
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
            ('created_at', str(datetime.datetime.now())),
            ('update_at', str(datetime.datetime.now())),
        ])
        local_spots.append(local_spot)

    data = OrderedDict([ ('local_spot', local_spots) ])
    return render_json_response(request, data)


@require_http_methods(["GET", "POST"])
def Local_environment(request):
    local_environments = []

    for environment in Environment.objects.all().order_by('environment_id'):

        spot_photo = Spot_photo.objects.all().filter(spot_id=environment.spot_id).first()
        if spot_photo is None:
            continue

        local_environment = OrderedDict([
            ('environment_id', environment.environment_id),
            ('weather', environment.weather),
            ('temperature', environment.temperature),
            ('created_at', str(datetime.datetime.now())),
            ('update_at', str(datetime.datetime.now())),
        ])
        local_environments.append(local_environment)

    data = OrderedDict([ ('local_environment', local_environments)])
    return render_json_response(request, data)


@require_http_methods(["GET", "POST"])
def Local_access_point(request):
    local_access_points = []

    for access_point in Access_point.objects.all().order_by('access_point_id'):

        spot_id = access_point.spot_id
        coordinate_id = access_point.coordinate_id
        message_id = access_point.message_id

        environment = Environment.objects.all().filter(spot_id=spot_id).first()
        if environment is None:
            continue
        spot_photo = Spot_photo.objects.all().filter(spot_id=spot_id).first()
        if spot_photo is None:
            continue
        character_data = Character_data.objects.all().filter(access_point_id=access_point.access_point_id).first()
        if character_data is None:
            continue
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
            ('created_at', str(datetime.datetime.now())),
            ('update_at', str(datetime.datetime.now())),
        ])
        local_access_points.append(local_access_point)

    data = OrderedDict([('local_access_point', local_access_points)])
    return render_json_response(request, data)


@require_http_methods(["GET", "POST"])
def Local_character(request):
    local_characters = []

    for character_data in Character_data.objects.all().order_by('character_data_id'):

        access_point_id = character_data.access_point_id
        access_point = Access_point.objects.all().filter(access_point_id=access_point_id).first()
        environment = Environment.objects.all().filter(spot_id=access_point.spot_id).first()
        if environment is None:
            continue
        spot_photo = Spot_photo.objects.all().filter(spot_id=access_point.spot_id).first()
        if spot_photo is None:
            continue
        if character_data is None:
            continue

        weather = environment.weather

        if character_data.weather_condition == "晴天":
            #晴天時の条件
            print(weather)
            if weather != "晴れ" and weather != "曇り":
                continue
        else:
            #雨天時の条件
            if weather == "晴れ" or weather == "曇り":
                continue

        character_id = character_data.character_id
        character = Character.objects.all().filter(character_id=character_id).first()

        local_character = OrderedDict([
            ('access_point_id', access_point.access_point_id),
            ('character_name', character.character_name),
            ('character_file_path', character_data.character_file_pass),
            ('created_at', str(datetime.datetime.now())),
            ('update_at', str(datetime.datetime.now())),
        ])
        local_characters.append(local_character)

    data = OrderedDict([('local_character', local_characters)])
    return render_json_response(request, data)
