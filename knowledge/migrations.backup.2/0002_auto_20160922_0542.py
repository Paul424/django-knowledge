# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('knowledge', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='alert',
            field=models.BooleanField(default=True, help_text='Check this if you want to be alerted when a new response is added.', verbose_name='Alert'),
        ),
        migrations.AlterField(
            model_name='response',
            name='alert',
            field=models.BooleanField(default=True, help_text='Check this if you want to be alerted when a new response is added.', verbose_name='Alert'),
        ),
    ]
