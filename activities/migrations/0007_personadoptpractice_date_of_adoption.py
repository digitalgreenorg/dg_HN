# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0006_remove_personadoptpractice_date_of_adoption'),
    ]

    operations = [
        migrations.AddField(
            model_name='personadoptpractice',
            name='date_of_adoption',
            field=models.DateField(null=True, blank=True),
        ),
    ]
