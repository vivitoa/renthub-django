from django.db import models
from django.core.validators import MinLengthValidator
from common.models import TimestampedModel
from catalog.models import Item
# Create your models here.

class Reservation(TimestampedModel):
    customer_name = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(2, "Customer name must be at least 2 characters long"),
        ]
    )
    customer_email = models.EmailField()
    start_date = models.DateField()
    end_date = models.DateField()
    items = models.ManyToManyField(Item, related_name='reservations')

    @property
    def total_price(self):
        days = (self.end_date - self.start_date).days
        if days == 0:
            days = 1
        total_items_price = sum(item.price_per_day for item in self.items.all())
        return days * total_items_price

    def __str__(self):
        return f"Reservation by {self.customer_name} from {self.start_date} to {self.end_date}"

