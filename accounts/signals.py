from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from accounts.models import Profile

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def create_profile_on_register(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(
            pk=instance.pk,
        )
        send_mail(
            subject="Welcome to RentHub!",
            message=(
                f"Hello! Your account has been created successfully.\n\n"
                f"Start exploring items available for rent at RentHub.\n\n"
                f"Happy renting!"
            ),
            from_email=settings.COMPANY_EMAIL,
            recipient_list=[instance.email],
            fail_silently=True,
        )
