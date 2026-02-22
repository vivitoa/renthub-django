from django.urls import path, include
from bookings import views


app_name = 'bookings'

urlpatterns = [
    path('', views.ReservationListView.as_view(), name='list'),
    path('create/', views.ReservationCreateView.as_view(), name='create'),
    path('<int:pk>/', include([
        path('', views.ReservationDetailView.as_view(), name='details'),
        path('edit/', views.ReservationUpdateView.as_view(), name='edit'),
        path('delete/', views.ReservationDeleteView.as_view(), name='delete'),
    ])),
]

