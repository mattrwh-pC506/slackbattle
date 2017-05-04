# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-04 15:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='armor_class',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='character_type',
            field=models.CharField(blank=True, choices=[('npc', 'NPC'), ('pc', 'PC'), ('monster', 'Monster')], max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='charisma',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='constitution',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='dexterity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='hit_points',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='intelligence',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='strength',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='wisdom',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]