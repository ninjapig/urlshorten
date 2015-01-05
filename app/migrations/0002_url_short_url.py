# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='short_url',
            field=models.CharField(default='google.com', max_length=200),
            preserve_default=False,
        ),
    ]
