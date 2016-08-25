# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0002_auto_20160810_2220'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='original_coco_id',
            field=models.BigIntegerField(null=True, editable=False),
        ),
        migrations.AddField(
            model_name='language',
            name='original_coco_id',
            field=models.BigIntegerField(null=True, editable=False),
        ),
        migrations.AddField(
            model_name='nonnegotiable',
            name='original_coco_id',
            field=models.BigIntegerField(null=True, editable=False),
        ),
        migrations.AddField(
            model_name='practice',
            name='original_coco_id',
            field=models.BigIntegerField(null=True, editable=False),
        ),
        migrations.AddField(
            model_name='practicesector',
            name='original_coco_id',
            field=models.BigIntegerField(null=True, editable=False),
        ),
        migrations.AddField(
            model_name='practicesubject',
            name='original_coco_id',
            field=models.BigIntegerField(null=True, editable=False),
        ),
        migrations.AddField(
            model_name='practicesubsector',
            name='original_coco_id',
            field=models.BigIntegerField(null=True, editable=False),
        ),
        migrations.AddField(
            model_name='practicesubtopic',
            name='original_coco_id',
            field=models.BigIntegerField(null=True, editable=False),
        ),
        migrations.AddField(
            model_name='practicetopic',
            name='original_coco_id',
            field=models.BigIntegerField(null=True, editable=False),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='original_coco_id',
            field=models.BigIntegerField(null=True, editable=False),
        ),
        migrations.AddField(
            model_name='video',
            name='original_coco_id',
            field=models.BigIntegerField(null=True, editable=False),
        ),
        migrations.AddField(
            model_name='videopractice',
            name='original_coco_id',
            field=models.BigIntegerField(null=True, editable=False),
        ),
    ]
