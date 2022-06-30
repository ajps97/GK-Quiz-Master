from django import forms
from .models import Question
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput


class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(widget=PasswordInput())


class QuestionAddForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ('question_text','choice_1','choice_2','choice_3','choice_4','answer','category','level')

class QuestionUpdateForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('question_text','choice_1','choice_2','choice_3','choice_4','answer','category','level')
