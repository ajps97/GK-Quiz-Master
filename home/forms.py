from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput


class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(widget=PasswordInput())


class SignupForm(UserCreationForm):


   # email = forms.EmailField(max_length=200,help_text='Required')

    class Meta:
        model = User
        fields = ('username','password1','password2')

class OtpForm(forms.Form):
    otp = forms.CharField(max_length=5,widget = PasswordInput())
