# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geographies', '0002_auto_20160819_1633'),
    ]

    operations = [
        migrations.AddField(
            model_name='block',
            name='original_coco_id',
            field=models.BigIntegerField(null=True, editable=False),
        ),
        migrations.AddField(
            model_name='country',
            name='original_coco_id',
            field=models.BigIntegerField(null=True, editable=False),
        ),
        migrations.AddField(
            model_name='district',
            name='original_coco_id',
            field=models.BigIntegerField(null=True, editable=False),
        ),
        migrations.AddField(
            model_name='state',
            name='original_coco_id',
            field=models.BigIntegerField(null=True, editable=False),
        ),
        migrations.AddField(
            model_name='village',
            name='original_coco_id',
            field=models.BigIntegerField(null=True, editable=False),
        ),
    ]
