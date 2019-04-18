from django.contrib import admin
from .models import Places


class PlacesAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'image_url')


admin.site.register(Places, PlacesAdmin)

