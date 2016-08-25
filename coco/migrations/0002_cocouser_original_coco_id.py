# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coco', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cocouser',
            name='original_coco_id',
            field=models.BigIntegerField(null=True, editable=False),
        ),
    ]
