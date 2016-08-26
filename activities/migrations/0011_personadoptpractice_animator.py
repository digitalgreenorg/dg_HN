# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_auto_20160822_1324'),
        ('activities', '0010_personadoptpractice_date_of_adoption'),
    ]

    operations = [
        migrations.AddField(
            model_name='personadoptpractice',
            name='animator',
            field=models.ForeignKey(blank=True, to='people.Animator', null=True),
        ),
    ]
