# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0004_auto_20160713_1319'),
    ]

    operations = [
        migrations.AddField(
            model_name='personadoptpractice',
            name='problem_faced',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='personadoptpractice',
            name='verification_status',
            field=models.IntegerField(default=0, choices=[(0, b'Not Checked'), (1, b'Approved'), (2, b'Rejected')], validators=[django.core.validators.MaxValueValidator(9)]),
        ),
        migrations.AlterField(
            model_name='personadoptpractice',
            name='verified_by',
            field=models.IntegerField(blank=True, choices=[(0, b'Digital Green'), (1, b'Partner'), (2, b'Third Party')], null=True, validators=[django.core.validators.MaxValueValidator(9)]),
        ),
        migrations.AlterField(
            model_name='screening',
            name='farmers_attendance',
            field=models.ManyToManyField(to='people.Person', through='activities.PersonMeetingAttendance', blank=b'False'),
        ),
        migrations.AlterField(
            model_name='screening',
            name='observation_status',
            field=models.IntegerField(default=0, choices=[(0, b'Not Observed'), (1, b'Observed')], validators=[django.core.validators.MaxValueValidator(9)]),
        ),
        migrations.AlterField(
            model_name='screening',
            name='observer',
            field=models.IntegerField(blank=True, choices=[(0, b'Digital Green'), (1, b'Partner'), (2, b'Third Party')], null=True, validators=[django.core.validators.MaxValueValidator(9)]),
        ),
    ]
