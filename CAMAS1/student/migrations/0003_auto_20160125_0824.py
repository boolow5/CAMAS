# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0001_initial'),
        ('student', '0002_auto_20160125_0711'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=300)),
            ],
        ),
        migrations.AddField(
            model_name='class',
            name='department',
            field=models.ForeignKey(default=None, to='university.Department'),
            preserve_default=False,
        ),
    ]
