from django.core import serializers
from django.core.management.base import BaseCommand
import json
from cms.models import (Message, Coordinate, Photo_path, Spot, Character,
                        Environment, Access_point, Character_data,
                        Spot_photo, Point_temperature, Spot_photo)
MODELS = (Message, Coordinate, Photo_path, Spot, Character,
        Environment, Access_point, Character_data,
        Spot_photo, Point_temperature, Spot_photo)

# BaseCommandを継承して作成
class Command(BaseCommand):
    # python manage.py help count_entryで表示されるメッセージ
    help = 'DBのデータを全てjsonに書き起こします'

    # コマンドが実行された際に呼ばれるメソッド
    def handle(self, *args, **options):
        datas = ""
        for model in MODELS:
            data = serializers.serialize("json", model.objects.all())
            if datas is "":
                datas = datas + data[1:-1]
            else:
                datas = datas + ", " + data[1:-1]

        datas = "[" + datas + "]"
        f = open("output.json", "w")
        f.write(datas)
        f.close()
        self.stdout.write(self.style.SUCCESS('Serializers compleat [output.json]'))
