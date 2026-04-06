from tkinter import CASCADE
from django.conf import settings
from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from common.models import TimestampedModel

# Create your models here.

class Item(TimestampedModel):
    class CategoryChoices(models.TextChoices):
        ELECTRONICS = 'Electronics', 'Electronics'
        TOOLS = 'Tools', 'Tools'
        VEHICLES = 'Vehicles', 'Vehicles'
        PARTY_EQUIPMENT = 'Party Equipment', 'Party Equipment'
    
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='items'
    )

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
    image = models.ImageField(
        upload_to='items/',
        blank=True,
        null=True,
        help_text="Upload an image file.",
    )
    category = models.CharField(
        max_length=50,
        choices=CategoryChoices.choices,
        default=CategoryChoices.TOOLS
    )

    def __str__(self):
        return self.title

class Review(TimestampedModel):

    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='reviews',
        null=True,
        blank=True
    )
    reviewer_name = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(2, "Name must be at least 2 characters.")]
    )
    rating = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1, "Minimum rating is 1"),
            MaxValueValidator(5, "Maximum rating is 5")
        ],
        help_text="Rating from 1 to 5"
    )
    comment = models.TextField()

    def __str__(self):
        return f"{self.rating}/5 for {self.item.title}"