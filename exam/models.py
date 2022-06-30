from django.db import models
from django.contrib.auth.models import User
from django.http.response import Http404
from quiz_master.models import Question
import uuid
# Create your models here.
MAX_SCORE=20
class Exam(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True,primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    attended = models.BooleanField(default=False)
    total_score = models.FloatField(default=20)
    obtained_score=models.FloatField(default=0)
    category=models.CharField(max_length=200,default='Mixed')

    def __str__(self):
        return f"{self.id} {self.user} [ {self.category} ] {self.created} "

    def createExam(user_id,category):
        generated_id=uuid.uuid4()
        user = User.objects.get(id=user_id)
        data=Exam(user=user,id=generated_id,category=category)
        data.save()
        exam = Exam.objects.get(id=generated_id)
        AnswerSheet.fillAnswersheet(Question.prepareQuestions(category),exam)
        return str(generated_id)
        
    def insertScore(score,exam_id):
        Exam.objects.filter(id=exam_id).update(obtained_score=score,attended=True)

    
class AnswerSheet(models.Model):

    exam = models.ForeignKey(Exam,on_delete=models.CASCADE)
    question_no = models.CharField(max_length=10,default='')
    question_text = models.CharField(max_length=200,default='')
    choice_1 = models.CharField(max_length=200,default='choice_1')
    choice_2 = models.CharField(max_length=200,default='choice_2')
    choice_3 = models.CharField(max_length=200,default='choice_3')
    choice_4 = models.CharField(max_length=200,default='choice_4')
    answer = models.CharField(max_length=200,default='')
    selected_choice = models.CharField(max_length=200,default='')
    


    def fillAnswersheet(question_obj_list,exam):
        for question_obj in question_obj_list:
            data = AnswerSheet(
            exam=exam,
            question_no = question_obj.id,
            question_text = question_obj.question_text,
            choice_1 = question_obj.choice_1,
            choice_2 = question_obj.choice_2,
            choice_3 = question_obj.choice_3,
            choice_4 = question_obj.choice_4,
            answer = question_obj.answer)
            data.save()
            
        #AnswerSheet.calculateScore(question_obj_list,answer_sheet)



    def saveAnswers(answers,exam_id):
        if Exam.objects.get(id=exam_id).attended:
            raise Http404
        else:
            for i in range(len(answers)):
                if answers[i]==None:
                    answers[i]="Not Answered"
                AnswerSheet.objects.filter(exam=exam_id,question_no=i+1).update(selected_choice=answers[i])
            Exam.insertScore(AnswerSheet.calculateScore(exam_id),exam_id)

    def calculateScore(exam_id):
        score=0
        qs=AnswerSheet.objects.filter(exam=exam_id)
        for object in qs:
            if object.answer==object.selected_choice:
                score+=1
        return score
   