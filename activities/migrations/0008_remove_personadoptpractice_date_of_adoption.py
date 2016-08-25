# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0007_personadoptpractice_date_of_adoption'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personadoptpractice',
            name='date_of_adoption',
        ),
    ]
