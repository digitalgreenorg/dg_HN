# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0009_auto_20160825_1120'),
    ]

    operations = [
        migrations.AddField(
            model_name='personadoptpractice',
            name='date_of_adoption',
            field=models.DateField(null=True, blank=True),
        ),
    ]
