# Generated by Django 3.2 on 2021-05-28 04:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0003_alter_profile_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='dob',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]