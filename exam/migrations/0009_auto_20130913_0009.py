# Generated by Django 3.2 on 2013-09-12 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0008_remove_exam_exam_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam',
            name='user',
        ),
        migrations.DeleteModel(
            name='AnswerSheet',
        ),
        migrations.DeleteModel(
            name='Exam',
        ),
    ]