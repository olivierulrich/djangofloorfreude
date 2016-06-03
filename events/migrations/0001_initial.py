# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-02 08:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField()),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('lineup', models.TextField()),
                ('startDate', models.DateTimeField()),
                ('endDate', models.DateTimeField()),
                ('price', models.IntegerField()),
                ('private', models.BooleanField(default=False)),
            ],
        ),
    ]
