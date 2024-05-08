from django import forms
from .models import Comment, Post



class SearchPost(forms.Form):
    search = forms.CharField(max_length=20)




class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('fullname','email','text',)


class ReplayForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['fullname','email','text', ]