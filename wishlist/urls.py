from django.urls import path
from wishlist import views

app_name = 'wishlist'

urlpatterns = [
    path('', views.WishlistView.as_view(), name='list'),
    path('toggle/<int:item_pk>/', views.toggle_wishlist_item, name='toggle'),
]

