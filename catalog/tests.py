from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse
from catalog.forms import ReviewCreateForm
from catalog.models import Item, Review

# Create your tests here.

UserModel = get_user_model()


class ItemModelTests(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create_user(
            email='owner@renthub.com',
            password='testpass123',
        )
        self.item = Item.objects.create(
            owner=self.user,
            title='Test Drill',
            description='A powerful drill for testing.',
            price_per_day=10.00,
            category='Tools',
        )

    def test_item_str_returns_title(self):
        self.assertEqual(str(self.item), 'Test Drill')

    def test_item_title_min_length_validation(self):
        item = Item(
            owner=self.user,
            title='A',
            description='Short title test.',
            price_per_day=5.00,
            category='Tools',
        )
        with self.assertRaises(ValidationError):
            item.full_clean()


class ReviewFormTests(TestCase):
    def test_review_form_valid_data(self):
        data = {
            'reviewer_name': 'Alex',
            'rating': 5,
            'comment': 'Excellent item, highly recommend!',
        }
        form = ReviewCreateForm(data=data)
        self.assertTrue(form.is_valid())

    def test_review_form_invalid_rating_above_max(self):
        data = {
            'reviewer_name': 'Alex',
            'rating': 6,
            'comment': 'Good item.',
        }
        form = ReviewCreateForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('rating', form.errors)

    def test_review_form_invalid_rating_below_min(self):
        data = {
            'reviewer_name': 'Alex',
            'rating': 0,
            'comment': 'Bad item.',
        }
        form = ReviewCreateForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('rating', form.errors)


class ItemViewTests(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create_user(
            email='viewer@renthub.com',
            password='testpass123',
        )
        self.item = Item.objects.create(
            owner=self.user,
            title='Test Scooter',
            description='Electric scooter for city commuting.',
            price_per_day=20.00,
            category='Vehicles',
        )

    def test_item_list_view_accessible_without_login(self):
        response = self.client.get(reverse('catalog:list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/item_list.html')

    def test_item_create_view_requires_login(self):
        response = self.client.get(reverse('catalog:create'))
        self.assertEqual(response.status_code, 302)
        self.assertIn('/accounts/login', response.url)

    def test_item_detail_view_returns_correct_item(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('catalog:details', kwargs={'pk': self.item.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Scooter')

