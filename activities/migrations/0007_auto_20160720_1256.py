# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0006_remove_personadoptpractice_problem_faced'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='influencers',
            unique_together=set([('date', 'mediator', 'village')]),
        ),
    ]
