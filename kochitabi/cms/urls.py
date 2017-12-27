from django.conf.urls import url
from rest_framework import routers
from .views import MessageViewSet, CoordinateViewSet, Photo_pathViewSet, SpotViewSet, CharacterViewSet, EnvironmentViewSet, Access_pointViewSet, Character_dataViewSet, Local_spotViewSet

#router = routers.SimpleRouter(trailing_slash=False)
router = routers.DefaultRouter() # DefaultRouterを通すと~/api/が開く
#simpleRouter = routers.SimpleRouter()
#router.register(r'test', TestViewSet, base_name='local')
#outer.register(r'test', TestViewSet.as_view(), base_name='test')
#outer.register(r'test', TestViewSet)
#router.registry(r'local_spot', Local_spotViewSet, base_naem='local_spot')
router.register(r'message', MessageViewSet)
router.register(r'coordinate', CoordinateViewSet)
router.register(r'photo_path', Photo_pathViewSet)
router.register(r'spot', SpotViewSet)
router.register(r'character', CharacterViewSet)
router.register(r'environment', EnvironmentViewSet)
router.register(r'access_point',Access_pointViewSet)
router.register(r'character_data', Character_dataViewSet)

urlpatterns = [
    # 書籍
    url(r'local_spot', Local_spotViewSet, name='local_spot'),     # 一覧
]

#router.register(r'test', TestViewSet)
#router.register(r'test', TestViewSet, base_name='test')
#router.register(r'test', TestViewSet)


#urlpatterns = [
    # 書籍
#    url(r'^v1/test/', TestViewSet, name='test'),      # 一覧
#]
