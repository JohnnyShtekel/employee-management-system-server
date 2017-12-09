# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-12-08 13:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('on vacation', 'OnVacation'), ('working', 'Working')], default='Working', max_length=20)),
                ('userName', models.CharField(max_length=100)),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
            ],
        ),
    ]