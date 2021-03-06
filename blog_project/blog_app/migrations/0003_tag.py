# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-03 14:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0002_auto_20160805_1056'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('articles', models.ManyToManyField(to='blog_app.Article')),
            ],
        ),
    ]
