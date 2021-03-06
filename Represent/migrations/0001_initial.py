# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-04-04 08:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Cat', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dog', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('password', models.CharField(blank=True, default=None, max_length=128, null=True)),
            ],
        ),
    ]
