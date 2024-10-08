# Generated by Django 5.0.1 on 2024-09-09 12:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education_Detailes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualification', models.CharField(max_length=15)),
                ('occupations', models.CharField(max_length=15)),
                ('occupation_Detailes', models.CharField(max_length=25)),
                ('annual_income', models.IntegerField()),
                ('employed_in', models.CharField(max_length=10)),
                ('working_location', models.CharField(max_length=15)),
                ('special_cases', models.CharField(max_length=15)),
                ('basic_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='education_details', to='app.basicinformation')),
            ],
        ),
    ]
