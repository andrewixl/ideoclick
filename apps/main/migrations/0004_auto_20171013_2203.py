# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-10-14 05:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_client_client_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='client_type',
            field=models.CharField(choices=[('normal', 'Normal'), ('large', 'Large')], max_length=256),
        ),
    ]