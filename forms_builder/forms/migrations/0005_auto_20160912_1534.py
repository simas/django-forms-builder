# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0004_form_registration_limit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='field',
            name='help_text',
            field=models.CharField(blank=True, verbose_name='Help text', max_length=1000),
        ),
    ]
