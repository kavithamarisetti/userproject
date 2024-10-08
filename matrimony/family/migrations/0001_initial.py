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
            name='FamilyDetailes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('family_values', models.CharField(max_length=50)),
                ('family_type', models.CharField(max_length=40)),
                ('family_status', models.CharField(max_length=100)),
                ('no_ofbroders', models.IntegerField()),
                ('no_ofbroders_married', models.IntegerField()),
                ('no_ofsisters', models.IntegerField()),
                ('no_ofsisters_married', models.IntegerField()),
                ('mothertounge', models.CharField(max_length=10)),
                ('fathername', models.CharField(max_length=50)),
                ('fatheroccupation', models.CharField(max_length=50)),
                ('mothername', models.CharField(max_length=40)),
                ('motheroccupation', models.CharField(max_length=50)),
                ('familywealth', models.TextField()),
                ('aboutfamily', models.TextField()),
                ('familystaychoice', models.CharField(choices=[('My parents will stay with me after marriage', 'My parents will stay with me after marriage'), ('My parents will not stay with me after marriage', 'My parents will not stay with me after marriage'), ('Dont wish to specify', 'Dont wish to specify')], max_length=50)),
                ('basic_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='family_details', to='app.basicinformation')),
            ],
        ),
    ]
