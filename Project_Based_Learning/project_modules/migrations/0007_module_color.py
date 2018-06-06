# Generated by Django 2.0.5 on 2018-06-04 14:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_modules', '0006_auto_20180604_1302'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='color',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(2), django.core.validators.MinValueValidator(0)]),
        ),
    ]
