from django import forms
from django.forms import widgets
from django.forms.widgets import RadioSelect
from django.http import request
from quiz_master.models import Question
SUBJECT_CHOICES = (
    ('Science','Science'),
    ('History','History'),
    ('General Knowledge','General Knowledge'),
    ('English','English'),
    ('Mixed','Mixed')
)




class ExamSettingsForm(forms.Form):
    subject = forms.ChoiceField(choices=SUBJECT_CHOICES)

'''
class ExamForm(forms.Form):
    question_obj_list=Question.prepareQuestions('Science')
    #question= forms.ChoiceField(widget=RadioSelect(),required=False)
   
    for question_obj in question_obj_list: 
        q1=forms.Field(label=question_obj.question_text,widget=RadioSelect(),required=False)
'''       
        
