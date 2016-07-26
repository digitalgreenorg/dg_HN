# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0005_auto_20160718_1218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personadoptpractice',
            name='problem_faced',
        ),
    ]
