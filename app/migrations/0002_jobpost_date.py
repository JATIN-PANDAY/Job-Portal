# Generated by Django 4.2.2 on 2023-06-15 11:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobpost',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
