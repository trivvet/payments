# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0003_supply_date_change'),
    ]

    operations = [
        migrations.AddField(
            model_name='supply',
            name='tariff',
            field=models.DecimalField(default=1, verbose_name='\u0422\u0430\u0440\u0438\u0444', max_digits=6, decimal_places=3),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='supply',
            name='arrears',
            field=models.DecimalField(verbose_name='\u0411\u0430\u043b\u0430\u043d\u0441 \u043d\u0430 \u0440\u0430\u0445\u0443\u043d\u043a\u0443', max_digits=6, decimal_places=2),
        ),
    ]
