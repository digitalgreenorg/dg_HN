# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0003_auto_20160822_1323'),
    ]

    operations = [
        migrations.AddField(
            model_name='screening',
            name='start_time',
            field=models.TimeField(null=True),
        ),
        migrations.AlterUniqueTogether(
            name='screening',
            unique_together=set([('date', 'animator', 'start_time', 'village')]),
        ),
    ]
