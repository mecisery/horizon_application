from django import forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

class RegistrationForm(forms.Form):
    username = forms.CharField(label='User name', max_length=20)
    email = forms.EmailField(label='Email', required=False)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Confirm', widget=forms.PasswordInput())
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(u'^[\u4e00-\u9fa5 _ a-zA-Z0-9]+$', username):
            raise forms.ValidationError(username)
        return username
    
    def clean_email(self):
        email = self.cleaned_data['email']
        return email

    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2:
                return password2
            raise forms.ValidationError('the password is not mathch !')

