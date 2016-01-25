# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='term',
            name='year',
        ),
        migrations.AlterField(
            model_name='classroom',
            name='name',
            field=models.CharField(max_length=30, default='One'),
        ),
    ]
