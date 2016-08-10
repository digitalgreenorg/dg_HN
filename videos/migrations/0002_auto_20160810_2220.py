# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('time_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('time_modified', models.DateTimeField(auto_now=True, null=True)),
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('category_name', models.CharField(unique=b'True', max_length=100)),
                ('user_created', models.ForeignKey(related_name='videos_category_created', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('user_modified', models.ForeignKey(related_name='videos_category_related_modified', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('time_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('time_modified', models.DateTimeField(auto_now=True, null=True)),
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('subcategory_name', models.CharField(max_length=100)),
                ('category', models.ForeignKey(to='videos.Category')),
                ('user_created', models.ForeignKey(related_name='videos_subcategory_created', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('user_modified', models.ForeignKey(related_name='videos_subcategory_related_modified', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name_plural': 'sub categories',
            },
        ),
        migrations.CreateModel(
            name='VideoPractice',
            fields=[
                ('time_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('time_modified', models.DateTimeField(auto_now=True, null=True)),
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('videopractice_name', models.CharField(max_length=100)),
                ('subcategory', models.ForeignKey(to='videos.SubCategory')),
                ('user_created', models.ForeignKey(related_name='videos_videopractice_created', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('user_modified', models.ForeignKey(related_name='videos_videopractice_related_modified', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='video',
            name='category',
            field=models.ForeignKey(blank=True, to='videos.Category', null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='subcategory',
            field=models.ForeignKey(blank=True, to='videos.SubCategory', null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='videopractice',
            field=models.ForeignKey(blank=True, to='videos.VideoPractice', null=True),
        ),
    ]
