
from django import forms

from service.models import ReserveService




class SearchTypeService(forms.Form):
    search = forms.CharField(max_length=20)


# class ReserveServiceForm(forms.Form):
#     firstname = forms.CharField(max_length=50)
#     lastname = forms.CharField(max_length=50)
#     email = forms.EmailField()
#     phone = forms.CharField(max_length=15)
#     # service = forms.CharField()  # Adjust this field based on your requirements
#     date = forms.DateField()
#     time = forms.TimeField()


class ReserveServiceForm(forms.ModelForm):
    class Meta:
        model = ReserveService
        fields = ['firstname','lastname', 'email','phone','date','time','service', ]