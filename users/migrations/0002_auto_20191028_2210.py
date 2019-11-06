# Generated by Django 2.1 on 2019-10-29 02:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')]),
        ),
    ]
