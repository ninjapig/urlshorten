# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_url_short_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='url',
            name='short_url',
        ),
        migrations.AddField(
            model_name='url',
            name='prefix',
            field=models.CharField(default='ten', max_length=200),
            preserve_default=False,
        ),
    ]
