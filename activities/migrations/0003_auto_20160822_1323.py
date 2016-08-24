# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0002_personadoptpractice_adopt_practice'),
    ]

    operations = [
        migrations.AddField(
            model_name='personadoptpractice',
            name='original_coco_id',
            field=models.BigIntegerField(null=True, editable=False),
        ),
        migrations.AddField(
            model_name='personmeetingattendance',
            name='original_coco_id',
            field=models.BigIntegerField(null=True, editable=False),
        ),
        migrations.AddField(
            model_name='screening',
            name='original_coco_id',
            field=models.BigIntegerField(null=True, editable=False),
        ),
    ]
