# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-10 02:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_auto_20170808_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='condition',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='model',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='shipping',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='features',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='long_description',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='manufacturer',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_info',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='short_description',
            field=models.TextField(blank=True, default='', max_length=150, null=True),
        ),
    ]