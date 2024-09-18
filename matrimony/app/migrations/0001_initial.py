# Generated by Django 5.0.1 on 2024-09-05 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BasicInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('mobile_number', models.CharField(max_length=15)),
                ('dob', models.DateField()),
                ('age', models.IntegerField()),
                ('height', models.DecimalField(decimal_places=2, max_digits=4)),
                ('blood_group', models.CharField(max_length=3)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('religion', models.CharField(max_length=100)),
                ('profile_created_by', models.CharField(max_length=100)),
                ('marital_status', models.CharField(choices=[('S', 'Single'), ('M', 'Married'), ('D', 'Divorced')], max_length=1)),
                ('your_religion', models.CharField(max_length=100)),
                ('your_caste', models.CharField(max_length=100)),
                ('sub_caste', models.CharField(blank=True, max_length=100)),
                ('about_yourself', models.TextField()),
            ],
        ),
    ]
