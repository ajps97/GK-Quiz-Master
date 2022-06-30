from django.urls import path

from . import views


app_name = 'quiz_master'
urlpatterns = [
    path('questions_view',views.questions_view,name='questions_view'),
    path('add_question',views.add_question,name='add_question'),
    path('delete_question/<int:question_id>/',views.delete_question,name='delete_question'),
    path('change_question/<int:question_id>/',views.change_question,name='change_question'),
    
]