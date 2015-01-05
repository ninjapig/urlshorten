# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20150104_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='prefix',
            field=models.CharField(default=b'', max_length=200),
            preserve_default=True,
        ),
    ]
