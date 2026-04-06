from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from catalog.models import Item
from wishlist.models import Wishlist

# Create your tests here.

UserModel = get_user_model()


class WishlistTests(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create_user(
            email='wishuser@renthub.com',
            password='testpass123',
        )
        self.item = Item.objects.create(
            owner=self.user,
            title='PS5',
            description='Gaming console.',
            price_per_day=15.00,
            category='Electronics',
        )

    def test_wishlist_auto_created_on_user_registration(self):
        self.assertTrue(Wishlist.objects.filter(user=self.user).exists())

    def test_wishlist_view_requires_login(self):
        response = self.client.get(reverse('wishlist:list'))
        self.assertEqual(response.status_code, 302)

    def test_toggle_adds_item_to_wishlist(self):
        self.client.force_login(self.user)
        self.client.post(reverse('wishlist:toggle', kwargs={'item_pk': self.item.pk}))
        self.assertIn(self.item, self.user.wishlist.items.all())

