from django import forms
from django.core.exceptions import ValidationError
from .models import Reservation


class ReservationCreateForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['customer_name', 'customer_email', 'start_date', 'end_date', 'items']
        labels = {
            'customer_name': 'Full Name',
            'customer_email': 'Email Address',
            'start_date': 'Pick-up Date',
            'end_date': 'Return Date',
            'items': 'Rented Items',
        }
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'items': forms.CheckboxSelectMultiple(),
        }
        error_messages = {
            'customer_name': {
                'required': 'Please enter your full name.',
            },
            'customer_email': {
                'invalid': 'Please enter a valid email address.',
            }
        }

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        if start_date and end_date and start_date >= end_date:
            raise ValidationError('End date must be after start date.')

        return cleaned_data

class ReservationUpdateForm(ReservationCreateForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['customer_email'].widget.attrs['readonly'] = True
        self.fields['customer_email'].help_text = "Email cannot be changed after reservation creation."

