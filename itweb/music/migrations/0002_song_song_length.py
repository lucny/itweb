# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-05 17:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='song_length',
            field=models.CharField(default='20', max_length=50),
            preserve_default=False,
        ),
    ]
