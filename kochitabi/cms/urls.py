from django.conf.urls import url
from .views import Local_spotViewSet, Local_environment, Local_access_point, Local_character
from .setweather import insert_weathers
from .settemperature import insert_temperature

#複合モデルによるjson出力用URL宣言
urlpatterns = [
    url(r'local_spot', Local_spotViewSet, name='local_spot'),
    url(r'local_environment', Local_environment, name='local_spot'),
    url(r'local_access_point', Local_access_point, name='local_spot'),
    url(r'local_character', Local_character, name='local_spot'),
    url(r'weather', insert_weathers, name='weather'),
    url(r'temperature', insert_temperature, name='temperature'),
]
