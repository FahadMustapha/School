# Generated by Django 4.1.2 on 2022-11-29 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tacher_name', models.CharField(max_length=50)),
                ('Gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=2)),
                ('Address', models.CharField(max_length=10)),
                ('Contact', models.CharField(max_length=10)),
            ],
        ),
    ]
