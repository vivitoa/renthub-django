from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Reservation
from .forms import ReservationCreateForm, ReservationUpdateForm
# Create your views here.


class ReservationListView(ListView):
    model = Reservation
    template_name = 'bookings/reservation_list.html'
    context_object_name = 'reservations'

class ReservationDetailView(DetailView):
    model = Reservation
    template_name = 'bookings/reservation_detail.html'
    context_object_name = 'reservation'

class ReservationCreateView(CreateView):
    model = Reservation
    form_class = ReservationCreateForm
    template_name = 'bookings/reservation_form.html'
    success_url = reverse_lazy('bookings:list')

class ReservationUpdateView(UpdateView):
    model = Reservation
    form_class = ReservationUpdateForm
    template_name = 'bookings/reservation_form.html'
    success_url = reverse_lazy('bookings:list')

class ReservationDeleteView(DeleteView):
    model = Reservation
    template_name = 'bookings/reservation_confirm_delete.html'
    success_url = reverse_lazy('bookings:list')

