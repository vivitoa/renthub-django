from rest_framework import generics, permissions
from bookings.models import Reservation
from bookings.serializers import ReservationSerializer
from common.permissions import IsOwnerOrReadOnly


class ReservationListAPIView(generics.ListCreateAPIView):
    serializer_class = ReservationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Reservation.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ReservationDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReservationSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        return Reservation.objects.filter(user=self.request.user)

