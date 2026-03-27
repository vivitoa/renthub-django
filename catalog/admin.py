from django.contrib import admin
from .models import Item, Review


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

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('item', 'reviewer_name', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('item__title', 'reviewer_name')

