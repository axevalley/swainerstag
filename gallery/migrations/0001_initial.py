# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-07 21:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='')),
                ('thumb', models.FileField(upload_to='')),
            ],
        ),
    ]
