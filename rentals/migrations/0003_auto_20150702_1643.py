# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0002_auto_20150702_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='copies',
            field=models.IntegerField(default=0),
        ),
    ]
