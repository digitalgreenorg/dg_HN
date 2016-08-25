# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0008_remove_personadoptpractice_date_of_adoption'),
    ]

    operations = [
        migrations.AlterField(
            model_name='screening',
            name='start_time',
            field=models.TimeField(auto_now_add=True, null=True),
        ),
    ]
