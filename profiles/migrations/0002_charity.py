# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Charity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('charity_name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=1000)),
                ('goal', models.IntegerField(default=0)),
                ('current', models.IntegerField(default=0)),
            ],
        ),
    ]
