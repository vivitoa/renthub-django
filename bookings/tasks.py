from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail


@shared_task
def send_reservation_confirmation(
        customer_name,
        customer_email,
        start_date,
        end_date,
        total_price,
):
    """
    Изпраща email потвърждение за резервация асинхронно.
    """
    subject = "RentHub — Reservation Confirmed!"
    message = (
        f"Hello {customer_name},\n\n"
        f"Your reservation has been confirmed!\n\n"
        f"Period: {start_date} → {end_date}\n"
        f"Total price: {total_price} EUR\n\n"
        f"Thank you for choosing RentHub!\n"
        f"The RentHub Team"
    )
    send_mail(
        subject=subject,
        message=message,
        from_email=settings.COMPANY_EMAIL,
        recipient_list=[customer_email],
        fail_silently=True,
    )
    return f"Confirmation email sent to {customer_email}"

