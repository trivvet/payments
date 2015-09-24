# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.

class Supply(models.Model):
	class Meta(object):
		verbose_name=u'Послуга'
		verbose_name_plural=u'Послуги'
	
	product_name = models.CharField(
		verbose_name=u'Назва послуги',
		max_length=30,
		blank=False)
	provider_name = models.CharField(
		verbose_name=u'Постачальник',
		max_length=40,
		blank=False)
	provider_site = models.URLField(
		verbose_name=u'Сайт постачальника',
		max_length=40,
		blank=True,
		null=True)
	"""counter 1"""
	counter_1_name = models.CharField(
		verbose_name=u'Назва Лічильника №1',
		max_length=10,
		blank=True,
		null=True)
	counter_1_indicator = models.IntegerField(
		verbose_name=u'Показники Лічильника №1',
		blank=True,
		null=True)
	"""counter 2"""
	counter_2_name = models.CharField(
		verbose_name=u'Назва Лічильника №2',
		max_length=10,
		blank=True,
		null=True)
	counter_2_indicator = models.IntegerField(
		verbose_name=u'Показники Лічильника №2',
		blank=True,
		null=True)
	"""counter 3"""
	counter_3_name = models.CharField(
		verbose_name=u'Назва Лічильника №3',
		max_length=10,
		blank=True,
		null=True)
	counter_3_indicator = models.IntegerField(
		verbose_name=u'Показники Лічильника №3',
		blank=True,
		null=True)
	"""counter 4"""
	counter_4_name = models.CharField(
		verbose_name=u'Назва Лічильника №4',
		max_length=10,
		blank=True,
		null=True)
	counter_4_indicator = models.IntegerField(
		verbose_name=u'Показники Лічильника №4',
		blank=True,
		null=True)
	arrears = models.DecimalField(
		verbose_name=u'Заборгованість',
		max_digits=6,
		decimal_places=2,
		blank=False)
	date_change = models.DateField(
		auto_now_add=True,
		verbose_name=u'Дата останньої зміни',
		editable=False,
		null=True)
		
	def __unicode__(self):
		return u"%s" % self.product_name
		
	
	
		
	
	
