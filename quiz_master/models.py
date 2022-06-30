import datetime
from django.db import models
from django.utils.timezone import now
import random

NUM_QUESTIONS=8

SUBJECT_LIST=['Science','History','General Knowledge','English']

SUBJECT_CHOICES = (
    ('Science','Science'),
    ('History','History'),
    ('General Knowledge','General Knowledge'),
    ('English','English'),
)
QUESTION_LEVEL = (
    ('Easy','Easy'),
    ('Medium','Medium'),
    ('Hard','Hard'),
)

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    choice_1 = models.CharField(max_length=200)
    choice_2 = models.CharField(max_length=200)
    choice_3 = models.CharField(max_length=200)
    choice_4 = models.CharField(max_length=200)
    answer   = models.CharField(max_length=200)
    category = models.CharField(max_length=200,default='General Knowledge',choices=SUBJECT_CHOICES)
    level = models.CharField(max_length=200,default='Easy',choices=QUESTION_LEVEL)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.question_text} [ {self.category} ] [ {self.level} ]"


    def prepareQuestions(subject):
        if subject=="Mixed":
            question_obj_list=[]

            for i in SUBJECT_LIST:
                
                qs=Question.objects.filter(category=i)
                question_obj_list.extend(random.sample(list(qs),int(NUM_QUESTIONS/len(SUBJECT_LIST))))
            count=1
            for j in question_obj_list:
                j.id=count
                count+=1
            return question_obj_list
        else:
            qs = Question.objects.filter(category=subject)
            question_obj_list=random.sample(list(qs),NUM_QUESTIONS)

            count=1
            for j in question_obj_list:
                j.id=count
                count+=1
                
            return question_obj_list