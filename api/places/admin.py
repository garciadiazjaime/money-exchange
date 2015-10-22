from django.contrib import admin

from .models import Place

class PlaceAdmin(admin.ModelAdmin):
	list_display = ('id', 'status', 'longitude', 'latitude')

admin.site.register(Place, PlaceAdmin)