# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20150104_1834'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='url',
            name='prefix',
        ),
    ]
