# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='supply',
            options={'verbose_name': '\u041f\u043e\u0441\u043b\u0443\u0433\u0430', 'verbose_name_plural': '\u041f\u043e\u0441\u043b\u0443\u0433\u0438'},
        ),
        migrations.AddField(
            model_name='supply',
            name='counter_1_indicator',
            field=models.IntegerField(null=True, verbose_name='\u041f\u043e\u043a\u0430\u0437\u043d\u0438\u043a\u0438 \u041b\u0456\u0447\u0438\u043b\u044c\u043d\u0438\u043a\u0430 \u21161', blank=True),
        ),
        migrations.AddField(
            model_name='supply',
            name='counter_1_name',
            field=models.CharField(max_length=10, null=True, verbose_name='\u041d\u0430\u0437\u0432\u0430 \u041b\u0456\u0447\u0438\u043b\u044c\u043d\u0438\u043a\u0430 \u21161', blank=True),
        ),
        migrations.AddField(
            model_name='supply',
            name='counter_2_indicator',
            field=models.IntegerField(null=True, verbose_name='\u041f\u043e\u043a\u0430\u0437\u043d\u0438\u043a\u0438 \u041b\u0456\u0447\u0438\u043b\u044c\u043d\u0438\u043a\u0430 \u21162', blank=True),
        ),
        migrations.AddField(
            model_name='supply',
            name='counter_2_name',
            field=models.CharField(max_length=10, null=True, verbose_name='\u041d\u0430\u0437\u0432\u0430 \u041b\u0456\u0447\u0438\u043b\u044c\u043d\u0438\u043a\u0430 \u21162', blank=True),
        ),
        migrations.AddField(
            model_name='supply',
            name='counter_3_indicator',
            field=models.IntegerField(null=True, verbose_name='\u041f\u043e\u043a\u0430\u0437\u043d\u0438\u043a\u0438 \u041b\u0456\u0447\u0438\u043b\u044c\u043d\u0438\u043a\u0430 \u21163', blank=True),
        ),
        migrations.AddField(
            model_name='supply',
            name='counter_3_name',
            field=models.CharField(max_length=10, null=True, verbose_name='\u041d\u0430\u0437\u0432\u0430 \u041b\u0456\u0447\u0438\u043b\u044c\u043d\u0438\u043a\u0430 \u21163', blank=True),
        ),
        migrations.AddField(
            model_name='supply',
            name='counter_4_indicator',
            field=models.IntegerField(null=True, verbose_name='\u041f\u043e\u043a\u0430\u0437\u043d\u0438\u043a\u0438 \u041b\u0456\u0447\u0438\u043b\u044c\u043d\u0438\u043a\u0430 \u21164', blank=True),
        ),
        migrations.AddField(
            model_name='supply',
            name='counter_4_name',
            field=models.CharField(max_length=10, null=True, verbose_name='\u041d\u0430\u0437\u0432\u0430 \u041b\u0456\u0447\u0438\u043b\u044c\u043d\u0438\u043a\u0430 \u21164', blank=True),
        ),
    ]
