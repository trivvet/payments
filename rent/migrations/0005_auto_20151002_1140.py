# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0004_auto_20151001_1807'),
    ]

    operations = [
        migrations.AddField(
            model_name='supply',
            name='account',
            field=models.IntegerField(null=True, verbose_name='\u041d\u043e\u043c\u0435\u0440 \u0440\u0430\u0445\u0443\u043d\u043a\u0443', blank=True),
        ),
        migrations.AlterField(
            model_name='supply',
            name='date_change',
            field=models.DateField(verbose_name='\u0414\u0430\u0442\u0430'),
        ),
    ]
