# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personadoptpractice',
            name='date_of_verification',
            field=models.DateField(null=True, blank=True),
        ),
    ]
