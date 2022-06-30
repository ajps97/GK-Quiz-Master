from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, Http404
from django.contrib import messages
from .forms import LoginForm, SignupForm
from random import randrange
from django.contrib.auth.models import User

# Create your views here.

def login_view(request):


	form = LoginForm(request.POST)
	if request.method == 'POST':
		user = authenticate(username=request.POST['username'], password=request.POST['password'])

		if user is not None:
			login(request,user)
			if user.is_superuser:
				return redirect('admin:index')

			if user.has_perm('quiz_master.add_question'):
				return redirect('quiz_master:questions_view')
			else:
				return redirect('user_profile:index')
		else:
			messages.warning(request,'Authentication failiure!')
			
	context = {'form':form}

	return render(request,'home/home.html',context)






def logout_view(request):
	
	logout(request)
	messages.warning(request,'Successfully logged out')
	return redirect('home:login_view')






def signup_view(request):
	
	form = SignupForm(request.POST)
	if request.method == 'POST':
		
		if form.is_valid():

			

			user = form.save()
			user.is_active = True
			user.save()
			user = authenticate(username=request.POST['username'], password=request.POST['password1'])
			request.session['username']=username=request.POST['username']
			
			return redirect('home:login_view')
			
			

	return render(request,'home/signup.html',{'form':form})






