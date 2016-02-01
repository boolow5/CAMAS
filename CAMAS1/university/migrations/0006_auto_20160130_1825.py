# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0005_classroom_department'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='DoBirth',
            new_name='DateOfBirth',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='fname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='lname',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='mname',
            new_name='middle_name',
        ),
        migrations.AlterField(
            model_name='student',
            name='classroom',
            field=models.ForeignKey(to='university.Classroom'),
        ),
    ]
