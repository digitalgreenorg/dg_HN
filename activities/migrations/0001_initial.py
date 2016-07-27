# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('geographies', '__first__'),
        ('videos', '__first__'),
        ('people', '__first__'),
        ('programs', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Influencers',
            fields=[
                ('time_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('time_modified', models.DateTimeField(auto_now=True, null=True)),
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('date', models.DateField()),
                ('number_of_male', models.IntegerField(null=True, blank=True)),
                ('number_of_female', models.IntegerField(null=True, blank=True)),
                ('group', models.ManyToManyField(to='people.PersonGroup')),
                ('mediator', models.ForeignKey(to='people.Animator')),
                ('partner', models.ForeignKey(to='programs.Partner')),
                ('user_created', models.ForeignKey(related_name='activities_influencers_created', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('user_modified', models.ForeignKey(related_name='activities_influencers_related_modified', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('video', models.ManyToManyField(to='videos.Video')),
                ('village', models.ForeignKey(to='geographies.Village')),
            ],
        ),
        migrations.CreateModel(
            name='PersonAdoptPractice',
            fields=[
                ('time_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('time_modified', models.DateTimeField(auto_now=True, null=True)),
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('verification_status', models.IntegerField(default=0, choices=[(0, b'Not Checked'), (1, b'Approved'), (2, b'Rejected')], validators=[django.core.validators.MaxValueValidator(9)])),
                ('non_negotiable_check', models.CharField(max_length=256, null=True, blank=True)),
                ('verified_by', models.IntegerField(blank=True, choices=[(0, b'Digital Green'), (1, b'Partner'), (2, b'Third Party')], null=True, validators=[django.core.validators.MaxValueValidator(9)])),
                ('date_of_verification', models.DateField(null=True, blank=True)),
                ('promote_practice', models.BooleanField(default=False)),
                ('n_one', models.BooleanField(default=False, db_index=True)),
                ('n_two', models.BooleanField(default=False, db_index=True)),
                ('n_three', models.BooleanField(default=False, db_index=True)),
                ('n_four', models.BooleanField(default=False, db_index=True)),
                ('n_five', models.BooleanField(default=False, db_index=True)),
                ('partner', models.ForeignKey(to='programs.Partner')),
                ('person', models.ForeignKey(to='people.Person')),
                ('user_created', models.ForeignKey(related_name='activities_personadoptpractice_created', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('user_modified', models.ForeignKey(related_name='activities_personadoptpractice_related_modified', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('video', models.ForeignKey(to='videos.Video')),
            ],
        ),
        migrations.CreateModel(
            name='PersonMeetingAttendance',
            fields=[
                ('time_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('time_modified', models.DateTimeField(auto_now=True, null=True)),
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('category', models.CharField(max_length=1, choices=[(0, b'Pregnant Woman'), (1, b'Mother of child < 5 years old'), (2, b'Adolescent girl (10-19 years old)'), (3, b'Other Female'), (4, b'Male')])),
                ('person', models.ForeignKey(to='people.Person')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Screening',
            fields=[
                ('time_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('time_modified', models.DateTimeField(auto_now=True, null=True)),
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('date', models.DateField()),
                ('location', models.CharField(max_length=200, blank=True)),
                ('observation_status', models.IntegerField(default=0, choices=[(0, b'Not Observed'), (1, b'Observed')], validators=[django.core.validators.MaxValueValidator(9)])),
                ('screening_grade', models.CharField(blank=True, max_length=1, null=True, choices=[(b'A', b'A'), (b'B', b'B'), (b'C', b'C'), (b'D', b'D')])),
                ('observer', models.IntegerField(blank=True, choices=[(0, b'Digital Green'), (1, b'Partner'), (2, b'Third Party')], null=True, validators=[django.core.validators.MaxValueValidator(9)])),
                ('problem_faced', models.TextField(blank=True)),
                ('animator', models.ForeignKey(to='people.Animator')),
                ('farmer_groups_targeted', models.ManyToManyField(to='people.PersonGroup')),
                ('farmers_attendance', models.ManyToManyField(to='people.Person', through='activities.PersonMeetingAttendance', blank=b'False')),
                ('partner', models.ForeignKey(to='programs.Partner')),
                ('user_created', models.ForeignKey(related_name='activities_screening_created', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('user_modified', models.ForeignKey(related_name='activities_screening_related_modified', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('videoes_screened', models.ManyToManyField(to='videos.Video')),
                ('village', models.ForeignKey(to='geographies.Village')),
            ],
        ),
        migrations.AddField(
            model_name='personmeetingattendance',
            name='screening',
            field=models.ForeignKey(to='activities.Screening'),
        ),
        migrations.AddField(
            model_name='personmeetingattendance',
            name='user_created',
            field=models.ForeignKey(related_name='activities_personmeetingattendance_created', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='personmeetingattendance',
            name='user_modified',
            field=models.ForeignKey(related_name='activities_personmeetingattendance_related_modified', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='screening',
            unique_together=set([('date', 'animator', 'village')]),
        ),
        migrations.AlterUniqueTogether(
            name='personadoptpractice',
            unique_together=set([('person', 'video', 'date_of_verification')]),
        ),
        migrations.AlterUniqueTogether(
            name='influencers',
            unique_together=set([('date', 'mediator', 'village')]),
        ),
    ]
