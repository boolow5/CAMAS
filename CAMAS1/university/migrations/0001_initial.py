# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.auth.models
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('number', models.IntegerField()),
                ('balance', models.DecimalField(default=0.0, decimal_places=2, max_digits=12)),
            ],
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('amount', models.DecimalField(default=0.0, decimal_places=2, max_digits=12)),
                ('description', models.TextField(max_length=300)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('account', models.ForeignKey(to='university.Account')),
            ],
        ),
        migrations.CreateModel(
            name='ClassRoom',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=30, default='One')),
                ('date_opened', models.DateField(default=django.utils.timezone.now)),
                ('max_year', models.IntegerField(default=4)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
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
                ('classroom', models.ForeignKey(to='university.ClassRoom')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, parent_link=True)),
                ('subject', models.ForeignKey(to='university.Subject')),
            ],
            options={
                'verbose_name': 'user',
                'abstract': False,
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('is_first', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('amount', models.DecimalField(default=0.0, decimal_places=2, max_digits=12)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('description', models.TextField(max_length=300)),
                ('is_debit', models.BooleanField(default=True)),
                ('payee', models.ForeignKey(to='university.Account')),
                ('received_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=30)),
                ('level', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='registered_by',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='faculty',
            name='dean',
            field=models.ForeignKey(to='university.Teacher'),
        ),
        migrations.AddField(
            model_name='department',
            name='faculty',
            field=models.ForeignKey(to='university.Faculty'),
        ),
        migrations.AddField(
            model_name='classroom',
            name='current_semester',
            field=models.ForeignKey(to='university.Term'),
        ),
        migrations.AddField(
            model_name='classroom',
            name='current_year',
            field=models.ForeignKey(to='university.Year'),
        ),
        migrations.AddField(
            model_name='account',
            name='owner',
            field=models.ForeignKey(to='university.Student'),
        ),
    ]
