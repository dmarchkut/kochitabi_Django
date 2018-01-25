from django.core import serializers
from django.core.management.base import BaseCommand
import json

# BaseCommandを継承して作成
class Command(BaseCommand):
    # python manage.py help count_entryで表示されるメッセージ
    help = '第1引数で入力したjsonファイルを読み込みます manage.pyからのパスを入力してください'

    # コマンドライン引数を指定します。(argparseモジュール https://docs.python.org/2.7/library/argparse.html)
    # 今回はblog_idという名前で取得する。（引数は最低でも1個, int型）
    def add_arguments(self, parser):
        parser.add_argument('jsonFile', nargs='+', type=str)


    # コマンドが実行された際に呼ばれるメソッド
    def handle(self, *args, **options):
        jsonFile = str(options['jsonFile'])
        jsonFile = jsonFile[2:-2]
        # print(open(options['jsonFile'])
        f=open(jsonFile, "r")
        for obj in serializers.deserialize("json", f):
            obj.save()
        f.close()

        # self.stdout.write(self.style.SUCCESS('OK'))
        self.stdout.write(self.style.SUCCESS('Deserialize compleat [%s]') %jsonFile)
