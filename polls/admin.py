from django.contrib import admin
from .models import UserInformation, Country, City


admin.site.register(UserInformation)
admin.site.register(Country)
admin.site.register(City)
