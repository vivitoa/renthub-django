from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import DetailView
from catalog.models import Item
from wishlist.models import Wishlist

# Create your views here.


class WishlistView(LoginRequiredMixin, DetailView):
    model = Wishlist
    template_name = 'wishlist/wishlist-page.html'
    context_object_name = 'wishlist'

    def get_object(self):
        return self.request.user.wishlist


def toggle_wishlist_item(request, item_pk):
    if not request.user.is_authenticated:
        return redirect('accounts:login')

    item = get_object_or_404(Item, pk=item_pk)
    wishlist = request.user.wishlist

    if item in wishlist.items.all():
        wishlist.items.remove(item)
    else:
        wishlist.items.add(item)

    return redirect(reverse('catalog:details', kwargs={'pk': item_pk}))

