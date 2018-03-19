# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-19 09:23
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import hs.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MainBoard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.CharField(max_length=12)),
                ('cover_photo', models.ImageField(default='cover_photo/ntnui-volleyball.png', upload_to=hs.models.get_cover_upload_to)),
            ],
        ),
        migrations.CreateModel(
            name='MainBoardMembership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateField(default=datetime.date.today)),
                ('role', models.CharField(max_length=30)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hs.MainBoard')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
