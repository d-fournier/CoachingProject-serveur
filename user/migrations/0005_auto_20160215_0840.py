# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-15 08:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20160212_1139'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='displayName',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='description',
            field=models.TextField(blank=True, max_length=400),
        ),
    ]
