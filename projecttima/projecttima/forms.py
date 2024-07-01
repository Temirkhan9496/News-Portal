
from ckeditor.fields import RichTextField
from django import forms
from .models import User, Advertisement
class AdForm(forms.ModelForm):
    content = RichTextField()

    class RegistrationForm(forms.ModelForm):
        class Meta:
            model = User
            fields = ['email']

    class AdvertisementForm(forms.ModelForm):
        class Meta:
            model = Advertisement
            fields = ['title', 'text', 'category']

