# Generated by Django 5.0.1 on 2024-09-05 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='show_permanent_address',
            field=models.TextField(default=False),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='show_working_address',
            field=models.TextField(default=False),
        ),
    ]
