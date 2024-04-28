


from django import forms


class SearchTypeService(forms.Form):
    search = forms.CharField(max_length=20)