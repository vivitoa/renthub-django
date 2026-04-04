from django.conf import settings
from django.db import models

# Create your models here.


class Wishlist(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='wishlist',
    )
    items = models.ManyToManyField(
        'catalog.Item',
        related_name='wishlisted_by',
        blank=True,
    )

    def __str__(self):
        return f"{self.user.email}'s wishlist"
