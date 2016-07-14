# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0003_auto_20160713_1212'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personadoptpractice',
            old_name='n1',
            new_name='n_five',
        ),
        migrations.RenameField(
            model_name='personadoptpractice',
            old_name='n2',
            new_name='n_four',
        ),
        migrations.RenameField(
            model_name='personadoptpractice',
            old_name='n3',
            new_name='n_one',
        ),
        migrations.RenameField(
            model_name='personadoptpractice',
            old_name='n4',
            new_name='n_three',
        ),
        migrations.RenameField(
            model_name='personadoptpractice',
            old_name='n5',
            new_name='n_two',
        ),
    ]
