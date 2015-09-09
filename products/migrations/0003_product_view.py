# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20150907_0529'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='view',
            field=models.IntegerField(default=1, help_text=b'Count views of a particular product', verbose_name=b'View', blank=True),
        ),
    ]
