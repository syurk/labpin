# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-24 22:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20170724_2049'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productimage',
            name='image',
        ),
    ]