# Generated by Django 4.2.2 on 2023-06-16 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_jobpost_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='contact',
            field=models.IntegerField(max_length=10),
        ),
    ]
