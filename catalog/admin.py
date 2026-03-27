from django.contrib import admin
from .models import Item
# Register your models here.


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'price_per_day']
    list_filter = ['category']
    search_fields = ['title', 'description']
    fieldsets = (
        ('General Information', {
            'fields': ('title', 'category', 'description')
        }),
        ('Pricing & Media', {
            'fields': ('price_per_day', 'image_url')
        }),
    )

