
from django import forms

from service.models import ReserveService,PersonService




class SearchTypeService(forms.Form):
    search = forms.CharField(max_length=20)



class ReserveServiceForm(forms.ModelForm):
    class Meta:
        model = ReserveService
        fields = ['firstname','lastname', 'email','phone','service','date','time', ]



# class PersonServiceForm(forms.ModelForm):
#     class Meta:
#         model = PersonService
    