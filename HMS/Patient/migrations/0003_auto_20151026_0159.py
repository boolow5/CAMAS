# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Patient', '0002_auto_20151023_1704'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('debit', models.DecimalField(default=0.0, max_digits=8, decimal_places=2)),
                ('credit', models.DecimalField(default=0.0, max_digits=8, decimal_places=2)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('person_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='Patient.Person')),
                ('registered_date', models.DateField(verbose_name=django.utils.timezone.now)),
                ('salary', models.DecimalField(default=0, max_digits=8, decimal_places=2)),
                ('user_type', models.TextField(default=b'Guest')),
            ],
            bases=('Patient.person',),
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='person_ptr',
        ),
        migrations.CreateModel(
            name='CustomerAccount',
            fields=[
                ('account_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='Patient.Account')),
                ('owner', models.ForeignKey(to='Patient.Patient')),
            ],
            bases=('Patient.account',),
        ),
        migrations.CreateModel(
            name='EmployeeAccount',
            fields=[
                ('account_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='Patient.Account')),
                ('owner', models.ForeignKey(to='Patient.Employee')),
            ],
            bases=('Patient.account',),
        ),
        migrations.AddField(
            model_name='doctor',
            name='employee_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, default=None, serialize=False, to='Patient.Employee'),
            preserve_default=False,
        ),
    ]
