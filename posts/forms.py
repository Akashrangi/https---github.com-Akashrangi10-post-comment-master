from django.contrib.auth.forms import UserCreationForm
from .models import AllUsers,Comments
from django import forms

class UserForm(UserCreationForm):
    class Meta:
        model = AllUsers
        fields = ['username','email','password1','password2']
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Your Username'}),
            'email':forms.TextInput(attrs={'class':'form-control','placeholder':'example@gmail.com '}),
            'password1':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}),
            'password2':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Conformation'}),
        }




class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ['post','name']
        labels = {'body':'Comments'}
        widgets = {
            'body':forms.TextInput(attrs={'placeholder':'Write a Comment Here'}),
        }

