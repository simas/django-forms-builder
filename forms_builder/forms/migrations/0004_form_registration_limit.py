# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0003_form_internal_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='registration_limit',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
