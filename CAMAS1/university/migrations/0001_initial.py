# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.contrib.auth.models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('number', models.IntegerField()),
                ('balance', models.DecimalField(decimal_places=2, max_digits=12, default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12, default=0.0)),
                ('description', models.TextField(max_length=300)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('account', models.ForeignKey(to='university.Account')),
            ],
        ),
        migrations.CreateModel(
            name='ClassRoom',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(default='One', max_length=30)),
                ('date_opened', models.DateField(default=django.utils.timezone.now)),
                ('max_year', models.IntegerField(default=4)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('user_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, parent_link=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('starting_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='ExamReport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('grade', models.DecimalField(decimal_places=2, max_digits=3, default=0.0)),
                ('note', models.TextField()),
                ('exam', models.ForeignKey(to='university.Exam')),
            ],
        ),
        migrations.CreateModel(
            name='ExamType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('max_marks', models.DecimalField(decimal_places=2, max_digits=3, default=100.0)),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=200)),
                ('dean', models.ForeignKey(to='university.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('level', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
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
                ('registered_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('is_first', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12, default=0.0)),
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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=30)),
                ('level', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='examreport',
            name='student',
            field=models.ForeignKey(to='university.Student'),
        ),
        migrations.AddField(
            model_name='examreport',
            name='subject',
            field=models.ForeignKey(to='university.Subject'),
        ),
        migrations.AddField(
            model_name='exam',
            name='type',
            field=models.ForeignKey(to='university.ExamType'),
        ),
        migrations.AddField(
            model_name='employee',
            name='position',
            field=models.ForeignKey(to='university.Position', null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='subject',
            field=models.ForeignKey(default=None, to='university.Subject'),
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
