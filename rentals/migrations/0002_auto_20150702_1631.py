# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='director',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='stars',
        ),
        migrations.AddField(
            model_name='person',
            name='movies',
            field=models.ForeignKey(to='rentals.Movie', blank=True, null=True),
        ),
    ]
