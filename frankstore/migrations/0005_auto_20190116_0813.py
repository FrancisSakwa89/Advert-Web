# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-16 05:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frankstore', '0004_auto_20190116_0807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='category',
            field=models.CharField(max_length=60),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]