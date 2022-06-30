# Generated by Django 3.2 on 2021-05-27 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_master', '0003_alter_question_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='category',
            field=models.CharField(choices=[('Mathematics', 'Mathematics'), ('Science', 'Science'), ('History', 'History'), ('General Knowledge', 'General Knowledge'), ('English', 'English')], default='General Knowledge', max_length=200),
        ),
    ]
