# Generated by Django 4.1.2 on 2022-11-29 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0003_subject_alter_class_class_teacher_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='Grades',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='result',
            name='Score',
            field=models.IntegerField(default=0),
        ),
    ]