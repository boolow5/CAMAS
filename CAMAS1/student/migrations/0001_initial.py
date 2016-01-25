# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.IntegerField()),
                ('balance', models.DecimalField(default=0.0, max_digits=12, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.DecimalField(default=0.0, max_digits=12, decimal_places=2)),
                ('description', models.TextField(max_length=300)),
                ('date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ClassRoom',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'One', max_length=30)),
                ('date_opened', models.DateField(default=django.utils.timezone.now)),
                ('max_year', models.IntegerField(default=4)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fname', models.CharField(max_length=30)),
                ('mname', models.CharField(max_length=30)),
                ('lname', models.CharField(max_length=30)),
                ('DoBirth', models.DateField()),
                ('address', models.TextField(default=None)),
                ('phone', models.CharField(max_length=30)),
                ('guardian', models.CharField(max_length=50)),
                ('guardian_phone', models.CharField(max_length=30)),
                ('status', models.BooleanField(default=False)),
                ('registered', models.DateField(default=django.utils.timezone.now)),
                ('last_updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('classroom', models.ForeignKey(to='student.ClassRoom')),
                ('registered_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_first', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.DecimalField(default=0.0, max_digits=12, decimal_places=2)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('description', models.TextField(max_length=300)),
                ('is_debit', models.BooleanField(default=True)),
                ('payee', models.ForeignKey(to='student.Student')),
                ('received_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('level', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='term',
            name='year',
            field=models.ForeignKey(to='student.Year'),
        ),
        migrations.AddField(
            model_name='classroom',
            name='current_semester',
            field=models.ForeignKey(to='student.Term'),
        ),
        migrations.AddField(
            model_name='classroom',
            name='current_year',
            field=models.ForeignKey(to='student.Year'),
        ),
        migrations.AddField(
            model_name='class',
            name='level',
            field=models.ForeignKey(to='student.Year'),
        ),
    ]
