# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-16 04:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frankstore', '0002_advert_prize'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advert',
            old_name='location',
            new_name='category',
        ),
    ]
