# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0002_auto_20160130_1700'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exam',
            old_name='type',
            new_name='e_type',
        ),
    ]
