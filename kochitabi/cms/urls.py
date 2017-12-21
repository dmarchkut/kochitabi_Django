from rest_framework import routers
from .views import MessageViewSet, CoordinateViewSet, Photo_pathViewSet, SpotViewSet, CharacterViewSet, EnvironmentViewSet, Access_pointViewSet, Character_dataViewSet


router = routers.DefaultRouter()
router.register(r'message', MessageViewSet)
router.register(r'coordinate', CoordinateViewSet)
router.register(r'photo_path', Photo_pathViewSet)
router.register(r'spot', SpotViewSet)
router.register(r'character', CharacterViewSet)
router.register(r'environment', EnvironmentViewSet)
router.register(r'access_point',Access_pointViewSet)
router.register(r'character_data', Character_dataViewSet)
