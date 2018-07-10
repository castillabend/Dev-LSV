# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-10 20:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Robotmintor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('started', models.DateTimeField(blank=True, null=True)),
                ('finished', models.DateTimeField(blank=True, null=True)),
                ('response', models.CharField(blank=True, max_length=250)),
                ('type', models.CharField(choices=[('1', 'robotA'), ('2', 'robotB')], default=1, max_length=50)),
                ('status', models.CharField(choices=[('1', 'Waiting'), ('2', 'Working'), ('3', 'Finished')], default=1, max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
