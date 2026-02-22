from django import forms
from .models import Item


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

