from django.contrib import admin
from core.models import Items

# Register your models here.

@admin.register(Items)
class ItemsAdmin(admin.ModelAdmin):
    list_display = ['name', 'brand', 'get_tags']

    def get_tags(self, obj):
        return ",".join(tag.name for tag in obj.tags.all())

    get_tags.short_description = 'Tags'