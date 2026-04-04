from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Reservation
from .forms import ReservationCreateForm, ReservationUpdateForm
from common.mixins import CheckUserIsOwner
# Create your views here.


class ReservationListView(LoginRequiredMixin, ListView):
    model = Reservation
    template_name = 'bookings/reservation_list.html'
    context_object_name = 'reservations'

    def get_queryset(self):
        return Reservation.objects.filter(user=self.request.user)

class ReservationDetailView(LoginRequiredMixin, CheckUserIsOwner, DetailView):
    model = Reservation
    template_name = 'bookings/reservation_detail.html'
    context_object_name = 'reservation'

class ReservationCreateView(LoginRequiredMixin, CreateView):
    model = Reservation
    form_class = ReservationCreateForm
    template_name = 'bookings/reservation_form.html'
    success_url = reverse_lazy('bookings:list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ReservationUpdateView(LoginRequiredMixin, CheckUserIsOwner, UpdateView):
    model = Reservation
    form_class = ReservationUpdateForm
    template_name = 'bookings/reservation_form.html'
    success_url = reverse_lazy('bookings:list')

class ReservationDeleteView(LoginRequiredMixin, CheckUserIsOwner, DeleteView):
    model = Reservation
    template_name = 'bookings/reservation_confirm_delete.html'
    success_url = reverse_lazy('bookings:list')

