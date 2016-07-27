# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0001_initial'),
        ('people', '0001_initial'),
        ('geographies', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('time_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('time_modified', models.DateTimeField(auto_now=True, null=True)),
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('language_name', models.CharField(unique=b'True', max_length=100)),
                ('user_created', models.ForeignKey(related_name='videos_language_created', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('user_modified', models.ForeignKey(related_name='videos_language_related_modified', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NonNegotiable',
            fields=[
                ('time_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('time_modified', models.DateTimeField(auto_now=True, null=True)),
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('non_negotiable', models.CharField(max_length=500)),
                ('physically_verifiable', models.BooleanField(default=False, db_index=True)),
                ('user_created', models.ForeignKey(related_name='videos_nonnegotiable_created', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('user_modified', models.ForeignKey(related_name='videos_nonnegotiable_related_modified', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Practice',
            fields=[
                ('time_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('time_modified', models.DateTimeField(auto_now=True, null=True)),
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('practice_name', models.CharField(max_length=200, null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Practice',
            },
        ),
        migrations.CreateModel(
            name='PracticeSector',
            fields=[
                ('time_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('time_modified', models.DateTimeField(auto_now=True, null=True)),
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=500)),
                ('user_created', models.ForeignKey(related_name='videos_practicesector_created', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('user_modified', models.ForeignKey(related_name='videos_practicesector_related_modified', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PracticeSubject',
            fields=[
                ('time_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('time_modified', models.DateTimeField(auto_now=True, null=True)),
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=500)),
                ('user_created', models.ForeignKey(related_name='videos_practicesubject_created', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('user_modified', models.ForeignKey(related_name='videos_practicesubject_related_modified', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PracticeSubSector',
            fields=[
                ('time_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('time_modified', models.DateTimeField(auto_now=True, null=True)),
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=500)),
                ('user_created', models.ForeignKey(related_name='videos_practicesubsector_created', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('user_modified', models.ForeignKey(related_name='videos_practicesubsector_related_modified', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PracticeSubtopic',
            fields=[
                ('time_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('time_modified', models.DateTimeField(auto_now=True, null=True)),
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=500)),
                ('user_created', models.ForeignKey(related_name='videos_practicesubtopic_created', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('user_modified', models.ForeignKey(related_name='videos_practicesubtopic_related_modified', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PracticeTopic',
            fields=[
                ('time_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('time_modified', models.DateTimeField(auto_now=True, null=True)),
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=500)),
                ('user_created', models.ForeignKey(related_name='videos_practicetopic_created', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('user_modified', models.ForeignKey(related_name='videos_practicetopic_related_modified', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('time_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('time_modified', models.DateTimeField(auto_now=True, null=True)),
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('video_type', models.IntegerField(choices=[(1, b'Demonstration'), (2, b'Success story/ Testimonial'), (3, b'Activity Introduction'), (4, b'Discussion'), (5, b'General Awareness')], validators=[django.core.validators.MaxValueValidator(9)])),
                ('duration', models.TimeField(null=True, blank=True)),
                ('benefit', models.TextField(blank=True)),
                ('production_date', models.DateField()),
                ('approval_date', models.DateField(null=True, blank=True)),
                ('youtubeid', models.CharField(max_length=20, blank=True)),
                ('review_status', models.IntegerField(default=0, choices=[(0, b'Not Reviewed'), (1, b'Reviewed')], validators=[django.core.validators.MaxValueValidator(9)])),
                ('video_grade', models.CharField(blank=True, max_length=1, null=True, choices=[(b'A', b'A'), (b'B', b'B'), (b'C', b'C')])),
                ('reviewer', models.IntegerField(blank=True, choices=[(0, b'Digital Green'), (1, b'Partner')], null=True, validators=[django.core.validators.MaxValueValidator(9)])),
                ('language', models.ForeignKey(to='videos.Language')),
                ('partner', models.ForeignKey(to='programs.Partner')),
                ('production_team', models.ManyToManyField(to='people.Animator')),
                ('related_practice', models.ForeignKey(blank=True, to='videos.Practice', null=True)),
                ('user_created', models.ForeignKey(related_name='videos_video_created', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('user_modified', models.ForeignKey(related_name='videos_video_related_modified', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('village', models.ForeignKey(to='geographies.Village')),
            ],
        ),
        migrations.AddField(
            model_name='practice',
            name='practice_sector',
            field=models.ForeignKey(default=1, to='videos.PracticeSector'),
        ),
        migrations.AddField(
            model_name='practice',
            name='practice_subject',
            field=models.ForeignKey(blank=True, to='videos.PracticeSubject', null=True),
        ),
        migrations.AddField(
            model_name='practice',
            name='practice_subsector',
            field=models.ForeignKey(blank=True, to='videos.PracticeSubSector', null=True),
        ),
        migrations.AddField(
            model_name='practice',
            name='practice_subtopic',
            field=models.ForeignKey(blank=True, to='videos.PracticeSubtopic', null=True),
        ),
        migrations.AddField(
            model_name='practice',
            name='practice_topic',
            field=models.ForeignKey(blank=True, to='videos.PracticeTopic', null=True),
        ),
        migrations.AddField(
            model_name='practice',
            name='user_created',
            field=models.ForeignKey(related_name='videos_practice_created', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='practice',
            name='user_modified',
            field=models.ForeignKey(related_name='videos_practice_related_modified', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='nonnegotiable',
            name='video',
            field=models.ForeignKey(to='videos.Video'),
        ),
        migrations.AlterUniqueTogether(
            name='video',
            unique_together=set([('title', 'production_date', 'language', 'village')]),
        ),
        migrations.AlterUniqueTogether(
            name='practice',
            unique_together=set([('practice_sector', 'practice_subsector', 'practice_topic', 'practice_subtopic', 'practice_subject')]),
        ),
    ]
