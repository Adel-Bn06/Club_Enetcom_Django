from django import forms
from .models import *

class add_member_form(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)
    Numero= forms.IntegerField()
    
    
class add_pres_form(forms.Form):
    username=forms.CharField(max_length=8)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)
    Numero= forms.IntegerField()
    club_name = forms.CharField(max_length=100)

class add_club(forms.Form):
    nom=forms.CharField(max_length=100)
    

class LoginForm(forms.Form):
    username = forms.CharField(label='username')
    password = forms.CharField(label='Password',widget=forms.PasswordInput)

class MessagesForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea)
    
class ActualiteForm(forms.ModelForm):
    class Meta:
        model = actualite
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titre'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}),
        }

   