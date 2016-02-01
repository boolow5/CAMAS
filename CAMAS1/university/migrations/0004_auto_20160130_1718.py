# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0003_auto_20160130_1711'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='is_admission',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='exam',
            name='starting_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
