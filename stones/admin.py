from django.contrib import admin
from .models import Stones


class StonesAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image_url')


admin.site.register(Stones, StonesAdmin)

