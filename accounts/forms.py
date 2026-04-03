from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from accounts.models import Profile

UserModel = get_user_model()


class AppUserCreationForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ['email']
        labels = {
            'email': 'Email Address',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = "At least 8 characters."
        self.fields['password2'].label = "Confirm Password"


class AppUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = UserModel


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'phone_number': 'Phone Number',
            'profile_picture': 'Profile Picture URL',
            'bio': 'About Me',
        }
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Tell others about yourself...'}),
            'phone_number': forms.TextInput(attrs={'placeholder': '+359 88 888 8888'}),
            'profile_picture': forms.URLInput(attrs={'placeholder': 'https://...'}),
        }
        help_texts = {
            'phone_number': 'Used for rental coordination.',
        }
