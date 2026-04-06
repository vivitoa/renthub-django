import datetime
from unittest.mock import patch
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from bookings.forms import ReservationCreateForm
from bookings.models import Reservation
from catalog.models import Item

# Create your tests here.

UserModel = get_user_model()


class ReservationModelTests(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create_user(
            email='renter@renthub.com',
            password='testpass123',
        )
        self.item = Item.objects.create(
            owner=self.user,
            title='Camera',
            description='Action camera.',
            price_per_day=12.00,
            category='Electronics',
        )
        self.reservation = Reservation.objects.create(
            user=self.user,
            customer_name='Test Renter',
            customer_email='renter@renthub.com',
            start_date=datetime.date(2026, 5, 1),
            end_date=datetime.date(2026, 5, 4),
        )
        self.reservation.items.add(self.item)

    def test_reservation_total_price_calculation(self):
        self.assertEqual(self.reservation.total_price, 36.00)

    def test_reservation_str(self):
        self.assertIn('Test Renter', str(self.reservation))


class ReservationFormTests(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create_user(
            email='formuser@renthub.com',
            password='testpass123',
        )
        self.item = Item.objects.create(
            owner=self.user,
            title='Drill',
            description='Power drill.',
            price_per_day=8.00,
            category='Tools',
        )

    def test_reservation_form_invalid_when_end_before_start(self):
        data = {
            'customer_name': 'John Doe',
            'customer_email': 'john@example.com',
            'start_date': '2026-05-10',
            'end_date': '2026-05-05',
            'items': [self.item.pk],
        }
        form = ReservationCreateForm(data=data)
        self.assertFalse(form.is_valid())

    def test_reservation_list_view_requires_login(self):
        response = self.client.get(reverse('bookings:list'))
        self.assertEqual(response.status_code, 302)
        self.assertIn('/accounts/login', response.url)

    @patch('bookings.views.send_reservation_confirmation.delay')
    def test_reservation_create_calls_celery_task(self, mock_task):
        self.client.force_login(self.user)
        data = {
            'customer_name': 'John Doe',
            'customer_email': 'john@example.com',
            'start_date': '2026-06-01',
            'end_date': '2026-06-05',
            'items': [self.item.pk],
        }
        self.client.post(reverse('bookings:create'), data)
        self.assertTrue(mock_task.called)

