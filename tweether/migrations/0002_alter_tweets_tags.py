# Generated by Django 3.2.4 on 2021-06-22 12:03

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweether', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweets',
            name='tags',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), null=True, size=None),
        ),
    ]
