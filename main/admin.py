from django.contrib import admin
from .models import DimHub

@admin.register(DimHub)
class DimHubAdmin(admin.ModelAdmin):
    list_display = ('hub_id', 'shortcode', 'name_en', 'username', 'creation_date')
    search_fields = ('name_en', 'username')
