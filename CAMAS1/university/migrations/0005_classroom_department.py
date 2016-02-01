# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0004_auto_20160130_1718'),
    ]

    operations = [
        migrations.AddField(
            model_name='classroom',
            name='department',
            field=models.ForeignKey(to='university.Department', null=True),
        ),
    ]
