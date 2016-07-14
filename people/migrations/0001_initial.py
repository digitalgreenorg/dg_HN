# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('geographies', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('programs', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animator',
            fields=[
                ('time_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('time_modified', models.DateTimeField(auto_now=True, null=True)),
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('phone_no', models.CharField(max_length=100, blank=True)),
                ('total_adoptions', models.PositiveIntegerField(default=0, editable=False, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='AnimatorAssignedVillage',
            fields=[
                ('time_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('time_modified', models.DateTimeField(auto_now=True, null=True)),
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('start_date', models.DateField(null=True, blank=True)),
                ('animator', models.ForeignKey(to='people.Animator')),
                ('user_created', models.ForeignKey(related_name='people_animatorassignedvillage_created', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('user_modified', models.ForeignKey(related_name='people_animatorassignedvillage_related_modified', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('village', models.ForeignKey(to='geographies.Village')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('time_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('time_modified', models.DateTimeField(auto_now=True, null=True)),
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('person_name', models.CharField(max_length=100)),
                ('father_name', models.CharField(max_length=100, blank=True)),
                ('age', models.IntegerField(max_length=3, null=True, blank=True)),
                ('gender', models.CharField(max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('phone_no', models.CharField(max_length=100, blank=True)),
                ('date_of_joining', models.DateField(null=True, blank=True)),
                ('image_exists', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PersonGroup',
            fields=[
                ('time_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('time_modified', models.DateTimeField(auto_now=True, null=True)),
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('group_name', models.CharField(max_length=100)),
                ('partner', models.ForeignKey(to='programs.Partner')),
                ('user_created', models.ForeignKey(related_name='people_persongroup_created', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('user_modified', models.ForeignKey(related_name='people_persongroup_related_modified', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('village', models.ForeignKey(to='geographies.Village')),
            ],
            options={
                'verbose_name': 'Person group',
            },
        ),
        migrations.AddField(
            model_name='person',
            name='group',
            field=models.ForeignKey(blank=True, to='people.PersonGroup', null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='partner',
            field=models.ForeignKey(to='programs.Partner'),
        ),
        migrations.AddField(
            model_name='person',
            name='user_created',
            field=models.ForeignKey(related_name='people_person_created', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='user_modified',
            field=models.ForeignKey(related_name='people_person_related_modified', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='village',
            field=models.ForeignKey(to='geographies.Village'),
        ),
        migrations.AddField(
            model_name='animator',
            name='assigned_villages',
            field=models.ManyToManyField(related_name='assigned_villages', null=True, through='people.AnimatorAssignedVillage', to='geographies.Village', blank=True),
        ),
        migrations.AddField(
            model_name='animator',
            name='district',
            field=models.ForeignKey(blank=True, to='geographies.District', null=True),
        ),
        migrations.AddField(
            model_name='animator',
            name='partner',
            field=models.ForeignKey(to='programs.Partner'),
        ),
        migrations.AddField(
            model_name='animator',
            name='user_created',
            field=models.ForeignKey(related_name='people_animator_created', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='animator',
            name='user_modified',
            field=models.ForeignKey(related_name='people_animator_related_modified', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='persongroup',
            unique_together=set([('group_name', 'village')]),
        ),
        migrations.AlterUniqueTogether(
            name='person',
            unique_together=set([('person_name', 'father_name', 'village')]),
        ),
        migrations.AlterUniqueTogether(
            name='animator',
            unique_together=set([('name', 'gender', 'partner', 'district')]),
        ),
    ]
