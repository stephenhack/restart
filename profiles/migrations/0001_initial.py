# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('years_of_service', models.CharField(max_length=200)),
                ('story', models.CharField(max_length=1000)),
                ('goal', models.IntegerField(default=0)),
                ('current', models.IntegerField(default=0)),
            ],
        ),
    ]
