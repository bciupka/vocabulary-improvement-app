# Generated by Django 4.2.5 on 2024-02-25 12:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('improver', '0007_link_random_nr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='word',
            field=models.CharField(max_length=255, validators=[django.core.validators.RegexValidator('^[a-zA-Z-]*$', 'Only letters allowed')]),
        ),
    ]