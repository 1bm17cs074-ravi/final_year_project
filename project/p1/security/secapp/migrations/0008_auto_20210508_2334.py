# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-05-08 18:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secapp', '0007_auto_20210508_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suspect_names',
            name='image',
            field=models.ImageField(blank=True, default='default/default_pic.jpg', null=True, upload_to='suspect_images/', verbose_name='img'),
        ),
        migrations.AlterField(
            model_name='suspect_names',
            name='last_pic',
            field=models.ImageField(blank=True, default='default/default_pic.jpg', null=True, upload_to='detect_images/', verbose_name='img'),
        ),
    ]
