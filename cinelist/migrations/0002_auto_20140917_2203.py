# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cinelist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cinema',
            name='tid',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
