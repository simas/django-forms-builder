# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0002_auto_20150721_1517'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='internal_name',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
