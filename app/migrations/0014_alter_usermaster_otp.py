# Generated by Django 4.1.1 on 2022-10-22 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_company_logo_pic_company_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermaster',
            name='otp',
            field=models.IntegerField(max_length=6),
        ),
    ]
