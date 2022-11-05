from django.contrib import admin
from .models import *

admin.site.register(Amenities)
admin.site.register(Hotel)
admin.site.register(HotelImages)
admin.site.register(HotelBooking)

admin.site.register(contactModel)