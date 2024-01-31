from django.utils.html import format_html
from django import forms
from backoffice.models import Contact
from django.core.exceptions import ValidationError

class EbookForm(forms.ModelForm):
    first_name = forms.CharField(
        required=True,
        min_length=3,
    )
    last_name = forms.CharField(
        required=True,
        min_length=3,
    )
    email = forms.EmailField(
        required=True,
    )

    phone = forms.CharField(
        required=False,
        label='Mobile'
    )

    status =  forms.BooleanField(
        label=format_html('I have read and agree to the <a href="terms-conditions/">Terms and Conditions</a>'),
        required=True,
    )
    
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'email', 'phone', 'status')

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if Contact.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise ValidationError('Email already exists.')
        return email
    
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')

        for char in phone:
            if not char.isdigit() and char != '+':
                raise ValidationError('Phone number should contain only digits or "+" symbol.')
        return phone
    
    def clean_status(self):
        status = self.cleaned_data.get('status')

        if not status:
            raise ValidationError('You must read and agree to the Terms and conditions')
        return status
    