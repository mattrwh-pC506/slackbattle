# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-04 04:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('character', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Encounter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('characters', models.ManyToManyField(to='character.Character')),
            ],
        ),
    ]
