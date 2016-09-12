# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0005_auto_20160912_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='field',
            name='placeholder_text',
            field=models.CharField(null=True, max_length=1000, blank=True, verbose_name='Placeholder Text'),
        ),
        migrations.AlterField(
            model_name='field',
            name='slug',
            field=models.SlugField(max_length=1000, blank=True, default='', verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='form',
            name='slug',
            field=models.SlugField(max_length=1000, unique=True, editable=False, verbose_name='Slug'),
        ),
    ]
