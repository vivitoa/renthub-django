from django.contrib import admin
from wishlist.models import Wishlist

# Register your models here.


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'item_count')
    search_fields = ('user__email',)

    def item_count(self, obj):
        return obj.items.count()
    item_count.short_description = 'Saved Items'

