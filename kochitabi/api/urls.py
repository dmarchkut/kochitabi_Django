from django.conf.urls import url
from .views import Local_spotViewSet, Local_environment, Local_access_point, Local_character


#複合モデルによるjson出力用URL宣言
urlpatterns = [
    url(r'local_spot', Local_spotViewSet, name='local_spot'),
    url(r'local_environment', Local_environment, name='local_spot'),
    url(r'local_access_point', Local_access_point, name='local_spot'),
    url(r'local_character', Local_character, name='local_spot'),
]
