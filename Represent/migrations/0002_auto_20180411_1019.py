# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-04-11 10:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Represent', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cat', to=settings.AUTH_USER_MODEL),
        ),
    ]
