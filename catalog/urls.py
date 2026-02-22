from django.urls import path, include
from catalog import views


app_name = 'catalog'

urlpatterns = [
    path('', views.ItemListView.as_view(), name='list'),
    path('create/', views.ItemCreateView.as_view(), name='create'),
    path('<int:pk>/', include([
        path('', views.ItemDetailView.as_view(), name='details'),
        path('edit/', views.ItemUpdateView.as_view(), name='edit'),
        path('delete/', views.ItemDeleteView.as_view(), name='delete'),
    ])),
]

