# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-15 10:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('relation', '0003_relation_relationisactive'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='relation',
            name='relationIsActive',
        ),
    ]