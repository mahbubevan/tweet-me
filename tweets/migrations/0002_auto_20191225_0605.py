# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-12-25 06:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweet',
            name='content2',
        ),
        migrations.RemoveField(
            model_name='tweet',
            name='content3',
        ),
    ]
