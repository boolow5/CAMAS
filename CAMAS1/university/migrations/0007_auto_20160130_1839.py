# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0006_auto_20160130_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examreport',
            name='grade',
            field=models.DecimalField(default=0.0, max_digits=5, decimal_places=2),
        ),
    ]
