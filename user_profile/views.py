from mysite.settings import MEDIA_ROOT, MEDIA_URL
from django.shortcuts import render
from django.db.models import Max,Count,Avg
from exam.models import Exam



# Create your views here.
def index(request):

	ags=Exam.objects.filter(user=request.user)
	t_score=ags.aggregate(Max('obtained_score'))
	t_num_exams=ags.aggregate(Count('id'))
	avg_score = ags.aggregate(Avg('obtained_score'))

	if t_score['obtained_score__max'] is None:
		top_score=0
	else:
		top_score=int(t_score['obtained_score__max'])

	if t_num_exams['id__count'] is None:
		num_exams=0
	else:
		num_exams=t_num_exams['id__count']
	if avg_score['obtained_score__avg'] is None:
		average_score = 0
	else:
		average_score = int(avg_score['obtained_score__avg'])
	context={'top_score':top_score,'num_exams':num_exams,'average_score':average_score}
	return render(request, 'profile_home.html',context)