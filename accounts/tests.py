from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from accounts.models import Profile

# Create your tests here.

UserModel = get_user_model()


class AppUserCreationTests(TestCase):
    def test_user_created_with_email(self):
        user = UserModel.objects.create_user(
            email='test@renthub.com',
            password='testpass123',
        )
        self.assertEqual(user.email, 'test@renthub.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)

    def test_profile_auto_created_on_user_registration(self):
        user = UserModel.objects.create_user(
            email='newuser@renthub.com',
            password='testpass123',
        )
        self.assertTrue(Profile.objects.filter(pk=user.pk).exists())

    def test_profile_linked_to_correct_user(self):
        user = UserModel.objects.create_user(
            email='profile@renthub.com',
            password='testpass123',
        )
        self.assertEqual(user.profile.user, user)


class RegisterViewTests(TestCase):
    def test_register_page_returns_200(self):
        response = self.client.get(reverse('accounts:register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/register-page.html')

    def test_register_creates_user_and_redirects(self):
        data = {
            'email': 'newuser@renthub.com',
            'password1': 'StrongPass123!',
            'password2': 'StrongPass123!',
        }
        response = self.client.post(reverse('accounts:register'), data)
        self.assertRedirects(response, reverse('accounts:login'))
        self.assertTrue(UserModel.objects.filter(email='newuser@renthub.com').exists())

    def test_profile_detail_requires_login(self):
        user = UserModel.objects.create_user(
            email='auth@renthub.com',
            password='testpass123',
        )
        response = self.client.get(reverse('accounts:details', kwargs={'pk': user.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertIn('/accounts/login', response.url)

