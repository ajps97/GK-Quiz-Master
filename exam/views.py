from django.forms import fields
from django.http import request
from django.http.response import Http404, HttpResponse
from django.shortcuts import redirect, render
from .forms import ExamSettingsForm
from django.contrib.auth.decorators import login_required
from .models import AnswerSheet, Exam

import random
# Create your views here.


NUM_QUESTIONS=8 #should be something divisible by 4 because there is 4 categories


# index view

@login_required
def index(request):
    
    if 'exam_id' in request.session:
        AnswerSheet.objects.filter(exam=request.session['exam_id']).delete()
    form = ExamSettingsForm(request.POST)
    if request.method == 'POST':
        category = request.POST.get('subject')
        request.session['exam_id']=Exam.createExam(request.user.id,category)
        
        return redirect('exam:test')
    context = {'form':form}
    
    return render(request,'exam/exam_home.html',context)


# test view

@login_required
def test(request):
    question_obj_list=AnswerSheet.objects.filter(exam=request.session['exam_id'])
    context = {'question_obj_list':question_obj_list}
    answers=[]
    if request.method == 'POST':
        for i in range(NUM_QUESTIONS):
            answers.insert(i,request.POST.get(str(i+1)))
    
        AnswerSheet.saveAnswers(answers,request.session['exam_id']) 
        return redirect('exam:result')
    return render(request,'exam/exam_main.html',context)




# the score view

def result(request):

    answers=AnswerSheet.objects.filter(exam=request.session['exam_id'])
    
    score=int((Exam.objects.get(id=request.session['exam_id'])).obtained_score)
    category=(Exam.objects.get(id=request.session['exam_id'])).category
    context={'answers':answers,'score':score,'category':category}
   # AnswerSheet.objects.filter(exam=request.session['exam_id']).delete()
    return render(request,'exam/results.html',context)
