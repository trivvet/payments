# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supply',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_name', models.CharField(max_length=30, verbose_name='\u041d\u0430\u0437\u0432\u0430 \u043f\u043e\u0441\u043b\u0443\u0433\u0438')),
                ('provider_name', models.CharField(max_length=40, verbose_name='\u041f\u043e\u0441\u0442\u0430\u0447\u0430\u043b\u044c\u043d\u0438\u043a')),
                ('provider_site', models.URLField(max_length=40, null=True, verbose_name='\u0421\u0430\u0439\u0442 \u043f\u043e\u0441\u0442\u0430\u0447\u0430\u043b\u044c\u043d\u0438\u043a\u0430', blank=True)),
                ('arrears', models.DecimalField(verbose_name='\u0417\u0430\u0431\u043e\u0440\u0433\u043e\u0432\u0430\u043d\u0456\u0441\u0442\u044c', max_digits=6, decimal_places=2)),
            ],
            options={
                'verbose_name': ('\u041f\u043e\u0441\u043b\u0443\u0433\u0430',),
                'verbose_name_plural': '\u041f\u043e\u0441\u043b\u0443\u0433\u0438',
            },
        ),
    ]
