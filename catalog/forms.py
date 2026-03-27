from django import forms
from .models import Item, Review


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['title', 'description', 'price_per_day', 'image_url', 'category']
        labels = {
            'title': 'Item Title',
            'description': 'Description',
            'price_per_day': 'Price per Day (EUR)',
            'image_url': 'Image URL',
            'category': 'Category',
        }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'e.g. PlayStation 5'}),
            'description': forms.Textarea(
                attrs={'placeholder': 'Describe the item condition and features...', 'rows': 4}),
            'image_url': forms.URLInput(attrs={'placeholder': 'https://...'}),
        }

class ReviewCreateForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['reviewer_name', 'rating', 'comment']
        labels = {
            'reviewer_name': 'Your Name',
            'rating': 'Rating (1-5 Stars)',
            'comment': 'Your Review',
        }
        widgets = {
            'reviewer_name': forms.TextInput(attrs={
                'placeholder': 'e.g. Alex',
                'class': 'form-control'
            }),
            'rating': forms.NumberInput(attrs={
                'min': 1,
                'max': 5,
                'class': 'form-control'
            }),
            'comment': forms.Textarea(attrs={
                'placeholder': 'Share your experience with this item...',
                'rows': 4,
                'class': 'form-control'
            }),
        }

