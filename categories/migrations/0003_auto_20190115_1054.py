# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-01-15 10:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_labelled_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='labelled_img',
            old_name='image_name',
            new_name='image_path',
        ),
    ]
