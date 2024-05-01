from django import forms
from pages.models import ContactUs


class ContactUSForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['fullname', 'email','phone','text', ]
