from django import forms
from .models import Post



class SearchPost(forms.Form):
    search = forms.CharField(max_length=20)