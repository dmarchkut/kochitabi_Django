from django.conf.urls import url
from .setweather import insert_weathers
from .settemperature import insert_temperature

#複合モデルによるjson出力用URL宣言
urlpatterns = [
    url(r'weather', insert_weathers, name='weather'),
    url(r'temperature', insert_temperature, name='temperature'),
]
