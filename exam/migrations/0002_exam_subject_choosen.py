# Generated by Django 3.2 on 2021-05-25 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='subject_choosen',
            field=models.CharField(default='Mixed', max_length=200),
        ),
    ]
