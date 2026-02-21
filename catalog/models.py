from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator
from common.models import TimestampedModel

# Create your models here.

class Category(TimestampedModel):
    name = models.CharField(
        max_length=100,
        unique=True,
        validators=[
            MinLengthValidator(2, "Category name must be at least 2 characters long"),
        ]
    )

    def __str__(self):
        return self.name

class Item(TimestampedModel):
    title = models.CharField(
        max_length=200,
        validators=[
            MinLengthValidator(2, "Title must be at least 2 characters long"),
        ]
    )
    description = models.TextField()
    price_per_day = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        default=0.0,
        validators=[
            MinValueValidator(0.0, "Price per day can`t be less than 0."),
        ]
    )
    image_url = models.URLField(
        blank=True,
        null=True,
        help_text="Image URL"
    )
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='items')

    def __str__(self):
        return self.title

