# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-09-26 19:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20190926_2213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data_database',
            name='data4',
        ),
        migrations.RemoveField(
            model_name='data_database',
            name='data5',
        ),
        migrations.RemoveField(
            model_name='data_database',
            name='data6',
        ),
        migrations.AlterField(
            model_name='data_database',
            name='publishing_date',
            field=models.DateTimeField(auto_now=True, verbose_name='yayin tarihi'),
        ),
    ]
