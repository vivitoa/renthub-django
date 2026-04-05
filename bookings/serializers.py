from rest_framework import serializers
from bookings.models import Reservation
from catalog.serializers import ItemSerializer


class ReservationSerializer(serializers.ModelSerializer):
    items_detail = ItemSerializer(source='items', many=True, read_only=True)
    total_price = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        read_only=True,
    )

    class Meta:
        model = Reservation
        fields = [
            'id', 'customer_name', 'customer_email',
            'start_date', 'end_date', 'items',
            'items_detail', 'total_price', 'created_at',
        ]
        read_only_fields = ['created_at', 'total_price']
        extra_kwargs = {
            'items': {'write_only': True},
        }

    def validate(self, data):
        start = data.get('start_date')
        end = data.get('end_date')
        if start and end and start >= end:
            raise serializers.ValidationError("End date must be after start date.")
        return data

