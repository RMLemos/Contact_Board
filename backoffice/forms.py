from django import forms
from django.core.exceptions import ValidationError
from . import models

class ContactForm(forms.ModelForm):
    
    class Meta:
        model = models.Contact
        fields = ('first_name', 'last_name', 'phone', 'email', 'category', 'city', 'country',)

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if models.Contact.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise ValidationError('Email already exists.')
        return email
    
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')

        for char in phone:
            if not char.isdigit() and char != '+':
                raise ValidationError('Phone number should contain only digits or "+" symbol.')
        return phone