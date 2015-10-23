# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Patient', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='customer',
        ),
        migrations.AddField(
            model_name='appointment',
            name='is_done',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Account',
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
    ]
