# Generated by Django 4.1.1 on 2022-10-22 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_alter_usermaster_otp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='dob',
            field=models.IntegerField(),
        ),
    ]
