from django.conf.urls import url
from rest_framework import routers
from .views import MessageViewSet, CoordinateViewSet, Photo_pathViewSet, SpotViewSet, CharacterViewSet, EnvironmentViewSet, Access_pointViewSet, Character_dataViewSet, Local_spotViewSet, Local_environment, Local_access_point, Local_character

#RESTフレームによるURL宣言
router = routers.DefaultRouter() # DefaultRouterを通すと~/api/が開く
router.register(r'message', MessageViewSet)
router.register(r'coordinate', CoordinateViewSet)
router.register(r'photo_path', Photo_pathViewSet)
router.register(r'spot', SpotViewSet)
router.register(r'character', CharacterViewSet)
router.register(r'environment', EnvironmentViewSet)
router.register(r'access_point',Access_pointViewSet)
router.register(r'character_data', Character_dataViewSet)
#複合モデルによるjson出力用URL宣言
urlpatterns = [
    url(r'local_spot', Local_spotViewSet, name='local_spot'),
    url(r'local_environment', Local_environment, name='local_spot'),
    url(r'local_access_point', Local_access_point, name='local_spot'),
    url(r'local_character', Local_character, name='local_spot'),
]
