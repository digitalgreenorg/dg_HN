# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('time_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('time_modified', models.DateTimeField(auto_now=True, null=True)),
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('block_name', models.CharField(unique=b'True', max_length=100)),
                ('start_date', models.DateField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('time_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('time_modified', models.DateTimeField(auto_now=True, null=True)),
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('country_name', models.CharField(unique=b'True', max_length=100)),
                ('start_date', models.DateField(null=True, blank=True)),
                ('user_created', models.ForeignKey(related_name='geographies_country_created', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('user_modified', models.ForeignKey(related_name='geographies_country_related_modified', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name_plural': 'countries',
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('time_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('time_modified', models.DateTimeField(auto_now=True, null=True)),
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('district_name', models.CharField(unique=b'True', max_length=100)),
                ('start_date', models.DateField(null=True, blank=True)),
                ('latitude', models.DecimalField(blank=True, null=True, max_digits=31, decimal_places=28, validators=[django.core.validators.MaxValueValidator(90), django.core.validators.MinValueValidator(-90)])),
                ('longitude', models.DecimalField(blank=True, null=True, max_digits=32, decimal_places=28, validators=[django.core.validators.MaxValueValidator(180), django.core.validators.MinValueValidator(-180)])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('time_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('time_modified', models.DateTimeField(auto_now=True, null=True)),
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('state_name', models.CharField(unique=b'True', max_length=100)),
                ('start_date', models.DateField(null=True, blank=True)),
                ('country', models.ForeignKey(to='geographies.Country')),
                ('user_created', models.ForeignKey(related_name='geographies_state_created', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('user_modified', models.ForeignKey(related_name='geographies_state_related_modified', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Village',
            fields=[
                ('time_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('time_modified', models.DateTimeField(auto_now=True, null=True)),
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('village_name', models.CharField(max_length=100)),
                ('start_date', models.DateField(null=True, blank=True)),
                ('latitude', models.CharField(max_length=25, null=True, blank=True)),
                ('longitude', models.CharField(max_length=25, null=True, blank=True)),
                ('grade', models.CharField(max_length=1, null=True, blank=True)),
                ('block', models.ForeignKey(to='geographies.Block')),
                ('user_created', models.ForeignKey(related_name='geographies_village_created', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('user_modified', models.ForeignKey(related_name='geographies_village_related_modified', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='district',
            name='state',
            field=models.ForeignKey(to='geographies.State'),
        ),
        migrations.AddField(
            model_name='district',
            name='user_created',
            field=models.ForeignKey(related_name='geographies_district_created', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='district',
            name='user_modified',
            field=models.ForeignKey(related_name='geographies_district_related_modified', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='block',
            name='district',
            field=models.ForeignKey(to='geographies.District'),
        ),
        migrations.AddField(
            model_name='block',
            name='user_created',
            field=models.ForeignKey(related_name='geographies_block_created', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='block',
            name='user_modified',
            field=models.ForeignKey(related_name='geographies_block_related_modified', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='village',
            unique_together=set([('village_name', 'block')]),
        ),
    ]
