from django.contrib import admin
from cms.models import (Message, Coordinate, Photo_path, Spot, Character,
                        Environment, Access_point, Character_data, Spot_photo, Point_temperature)

admin.site.register(Access_point)
admin.site.register(Character)
admin.site.register(Character_data)
admin.site.register(Coordinate)
admin.site.register(Environment)
admin.site.register(Message)
admin.site.register(Photo_path)
admin.site.register(Point_temperature)
admin.site.register(Spot)
admin.site.register(Spot_photo)
