from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import MinLengthValidator
from django.db import models
from accounts.managers import AppUserManager

# Create your models here.


class AppUser(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = "email"

    email = models.EmailField(
        unique=True,
    )

    is_active = models.BooleanField(
        default=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    objects = AppUserManager()

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(
        AppUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    first_name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        validators=[MinLengthValidator(2, "First name must be at least 2 characters.")],
    )

    last_name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        validators=[MinLengthValidator(2, "Last name must be at least 2 characters.")],
    )

    phone_number = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        help_text="Contact number for rental coordination.",
    )

    profile_picture = models.URLField(
        blank=True,
        null=True,
        help_text="URL to your profile picture.",
    )

    bio = models.TextField(
        blank=True,
        null=True,
        help_text="Tell others a bit about yourself.",
    )

    @property
    def get_full_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.user.email

    def __str__(self):
        return f"Profile of {self.user.email}"

