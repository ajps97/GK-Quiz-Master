# Generated by Django 3.2 on 2013-09-12 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0007_auto_20210530_2312'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam',
            name='exam_id',
        ),
    ]
