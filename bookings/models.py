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

    def __str__(self):
        return f"Reservation by {self.customer_name} from {self.start_date} to {self.end_date}"

