from django import forms
from .models import Post,Neighbourhood,User,Business

class UserForm (forms.ModelForm):
    class Meta:
        model = User
        exclude = ['user']


class PostForm(forms.ModelForm):
    class Meta: 
        model = Post       
        exclude = ['user']