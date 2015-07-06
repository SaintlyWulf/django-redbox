# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0003_auto_20150702_1643'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='release_year',
        ),
        migrations.AddField(
            model_name='movie',
            name='release_date',
            field=models.DateField(default=datetime.datetime(2015, 7, 6, 12, 53, 54, 461782)),
        ),
        migrations.AddField(
            model_name='person',
            name='gender',
            field=models.CharField(max_length=1, default='U', choices=[('M', 'Male'), ('F', 'Female'), ('U', 'Unknown')]),
        ),
        migrations.AlterField(
            model_name='movie',
            name='copies',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
    ]
