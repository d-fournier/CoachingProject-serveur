# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-29 14:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0005_message_ispinned'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='isPinned',
            new_name='is_pinned',
        ),
    ]