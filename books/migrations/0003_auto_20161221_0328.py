# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-21 03:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_blogmodel_desc'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='blogmodel',
            table='books_blog',
        ),
    ]