from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from wishlist.models import Wishlist

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def create_wishlist_on_register(sender, instance, created, **kwargs):
    if created:
        Wishlist.objects.create(user=instance)
