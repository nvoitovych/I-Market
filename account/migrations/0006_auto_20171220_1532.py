# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-20 15:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20171219_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='postal_code',
            field=models.CharField(blank=True, default='76000', max_length=20, null=True, verbose_name='Postal code'),
        ),
    ]