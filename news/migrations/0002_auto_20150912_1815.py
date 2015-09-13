# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='author',
            field=models.CharField(default=0, max_length=70),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='articles',
            name='heading',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
