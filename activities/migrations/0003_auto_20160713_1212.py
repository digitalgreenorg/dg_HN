# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0002_auto_20160712_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personadoptpractice',
            name='n1',
            field=models.BooleanField(default=False, db_index=True),
        ),
        migrations.AlterField(
            model_name='personadoptpractice',
            name='n2',
            field=models.BooleanField(default=False, db_index=True),
        ),
        migrations.AlterField(
            model_name='personadoptpractice',
            name='n3',
            field=models.BooleanField(default=False, db_index=True),
        ),
        migrations.AlterField(
            model_name='personadoptpractice',
            name='n4',
            field=models.BooleanField(default=False, db_index=True),
        ),
        migrations.AlterField(
            model_name='personadoptpractice',
            name='n5',
            field=models.BooleanField(default=False, db_index=True),
        ),
    ]
