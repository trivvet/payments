# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0002_auto_20150922_1311'),
    ]

    operations = [
        migrations.AddField(
            model_name='supply',
            name='date_change',
            field=models.DateField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u043e\u0441\u0442\u0430\u043d\u043d\u044c\u043e\u0457 \u0437\u043c\u0456\u043d\u0438', null=True),
        ),
    ]
