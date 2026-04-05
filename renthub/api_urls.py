from django.urls import path
from catalog.api_views import ItemListAPIView, ItemDetailAPIView
from bookings.api_views import ReservationListAPIView, ReservationDetailAPIView

urlpatterns = [
    path('items/', ItemListAPIView.as_view(), name='api-items-list'),
    path('items/<int:pk>/', ItemDetailAPIView.as_view(), name='api-items-detail'),
    path('reservations/', ReservationListAPIView.as_view(), name='api-reservations-list'),
    path('reservations/<int:pk>/', ReservationDetailAPIView.as_view(), name='api-reservation-detail'),
]

