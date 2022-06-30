from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, SUBJECT_LIST
from django.urls import reverse
from .forms import LoginForm,QuestionAddForm,QuestionUpdateForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import permission_required


@permission_required('quiz_master.add_question')

def questions_view(request):
	question_list=Question.objects.all()
	length=len(question_list)
	context={'question_list':question_list,'length':length,'category_list':SUBJECT_LIST}	
	return render(request, 'quiz_master/questions_view.html', context)

@permission_required('quiz_master.add_question')

def add_question(request):
	form = QuestionAddForm(request.POST)
	if request.method == 'POST':
		data=Question(question_text=request.POST['question_text'],
		choice_1=request.POST['choice_1'],
		choice_2=request.POST['choice_2'],
		choice_3=request.POST['choice_3'],
		choice_4=request.POST['choice_4'],
		answer=request.POST.get('answer'),
		category=request.POST.get('category'),
		level=request.POST.get('level'))
		data.save()
		return redirect('quiz_master:questions_view')
	return render(request,'quiz_master/add_question.html',{'form':form})
	



@permission_required('quiz_master.add_question')
def change_question(request,question_id):
	selected_question=get_object_or_404(Question,id=question_id)
	form = QuestionUpdateForm(instance=selected_question)

	if request.method == 'POST':
		selected_question.question_text=request.POST['question_text']
		selected_question.choice_1=request.POST['choice_1']
		selected_question.choice_2=request.POST['choice_2']
		selected_question.choice_3=request.POST['choice_3']
		selected_question.choice_4=request.POST['choice_4']
		selected_question.answer=request.POST.get('answer')
		selected_question.category=request.POST.get('category')
		selected_question.level=request.POST.get('level')
		selected_question.save()
		messages.warning(request,'Question updated')
		return redirect('quiz_master:questions_view')
	return render(request,'quiz_master/change_question.html',{'form':form})

@permission_required('quiz_master.add_question')
def delete_question(request,question_id):
	
	selected_question=Question.objects.get(id=question_id)
	selected_question.delete()
	messages.warning(request,'Question deleted')
	return redirect('quiz_master:questions_view')

	
