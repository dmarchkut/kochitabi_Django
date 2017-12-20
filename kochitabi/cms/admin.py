from django.contrib import admin

# Register your models here.
from .models import Access_point
from .models import Character
from .models import Character_data
from .models import Coordinate
from .models import Environment
from .models import Message
from .models import Photo_path
from .models import Point_temperature
from .models import Spot
from .models import Spot_photo

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
