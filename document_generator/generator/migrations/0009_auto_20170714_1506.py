# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-14 12:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0008_merge_20170714_0604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='course',
            field=models.IntegerField(null=True),
        ),
    ]