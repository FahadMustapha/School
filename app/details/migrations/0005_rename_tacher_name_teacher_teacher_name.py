# Generated by Django 4.1.2 on 2022-11-29 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0004_result_grades_result_score'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='Tacher_name',
            new_name='Teacher_name',
        ),
    ]
