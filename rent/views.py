# -*- coding: utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from .models import Supply
import pdb

# Create your views here.

def home(request):
	if Supply.objects.count() > 0:
		quantity = Supply.objects.distinct('product_name').count()
		supplies = Supply.objects.distinct('product_name').\
		  order_by('product_name', 'id').reverse()[0:quantity] 
		return render(request, 'rent/home.html', {'supplies': supplies})
	else: 
		return render(request, 'rent/home.html', {})
	
def add_product(request):
	if request.method == 'POST':
		if request.POST.get('cancel_button') is not None:
		  return HttpResponseRedirect(reverse('home'))
		elif request.POST.get('add_button') is not None:
		  data = {}
		  errors = {}
		  name_of_product = {
		    'water': u'Водопостачання',
		    'sewerage': u'Каналізація',
		    'electricity': u'Електропостачання',
		    'gas': u'Газопостачання',
		    'waste': u'Вивіз сміття'
		  }
		  product_name = request.POST.get('product_name', '').strip()
		  if not product_name:
			errors['product_name'] = u"Будь-ласка оберіть послугу"
		  if product_name not in name_of_product:
			errors['product_name'] = u"Будь ласка оберіть конкретну послугу"
		  else:
			if Supply.objects.filter(product_name=name_of_product[product_name]).count() > 0:
			  errors['product_name']= u"Ви вже додали дану послугу, виберіть іншу"
			data['product_name'] = name_of_product[product_name]
		  provider_name = request.POST.get('provider_name', '').strip()
		  data['provider_name'] = provider_name
		  provider_site = request.POST.get('provider_site', '').strip()
		  data['provider_site'] = provider_site
		  for i in range(1,5):
			counter_name = request.POST.get('counter_' + str(i) + '_name')
			counter_indicator = request.POST.get('counter_' + str(i) + '_indicator')
			if counter_name and counter_indicator:
				data['counter_' + str(i) + '_name'] = counter_name
				try:
					counter_indicator = int(counter_indicator)
					data['counter_' + str(i) + '_indicator'] = int(counter_indicator)
				except:
					errors['counter_' + str(i) + '_indicator'] = u"Будь-ласка введіть ціле число"
			elif (not counter_name) and counter_indicator:
				errors['counter_' + str(i) + '_name'] = u"Будь-ласка введіть назву лічильника"
				try:
					counter_indicator = int(counter_indicator)
					data['counter_' + str(i) + '_indicator'] = int(counter_indicator)
				except:
					errors['counter_' + str(i) + '_indicator'] = u"Будь-ласка введіть ціле число"
			elif counter_name and not counter_indicator:
				print 3
				errors['counter_' + str(i) + '_indicator'] = u"Будь-ласка введіть покази лічильника"
				data['counter_' + str(i) + '_name'] = counter_name
		  arrears = request.POST.get('arrears', '').strip()
		  if not arrears:
			errors['arrears'] = u'Будь-ласка введіть стан розрахунку'
		  else:
		    try:
			  arrears = int(arrears)
			  data['arrears'] = arrears
		    except:
			  errors['arrears'] = u"Будь-ласка введіть число"
		  if not errors:
		    product = Supply(**data)
		    product.save()
		    return HttpResponseRedirect(reverse('home'))
		  else:
		    return render(request, 'rent/add_product.html', {'data': data,
		      'errors': errors})
	else:
	  return render(request, 'rent/add_product.html', {})
		
def edit_indexes(request, pk):
	if request.method == 'POST':
		if request.POST.get('cancel_button') is not None:
		  return HttpResponseRedirect(reverse('home'))
		elif request.POST.get('save_button') is not None:
		  supply = Supply.objects.get(id=pk)
		  data = {}
		  errors = {}
		  data['id'] = supply.id
		  data['product_name'] = supply.product_name
		  data['provider_name'] = supply.provider_name
		  data['provider_site'] = supply.provider_site
		  for i in range(1,5):
			  exec('counter_name = supply.counter_%s_name' % i)
			  counter_indicator = request.POST.get('counter_' + str(i) + '_indicator')
			  if counter_name and counter_indicator:
				  data['counter_' + str(i) + '_name'] = counter_name
				  try:
					counter_indicator = int(counter_indicator)
					data['counter_' + str(i) + '_indicator'] = int(counter_indicator)
				  except:
					errors['counter_' + str(i) + '_indicator'] = u"Будь-ласка введіть ціле число"
			  elif counter_name and not counter_indicator:
				  errors['counter_' + str(i) + '_indicator'] = u"Будь-ласка введіть новий показник"
		  arrears = request.POST.get('arrears', '').strip()
		  if not arrears:
			  errors['arrears'] = u"Будь-ласка введіть стан розрахунку"
		  else:
			  try:
				  arrears = float(arrears)
				  data['arrears'] = arrears
			  except:
				  errors['arrears'] = u"Будь-ласка введіть число"
		  if not errors:
		    data['id'] = None
		    product = Supply(**data)
		    product.save()
		    return HttpResponseRedirect(reverse('home'))
		  else:
			return render(request, 'rent/edit_indexes.html', {'supply': data, 
			  'errors': errors})
	else:
		supply = Supply.objects.get(id=pk)
		return render(request, 'rent/edit_indexes.html', {'supply': supply})
		
def list_product(request, pk):
	product = Supply.objects.get(pk=pk)
	supplies = Supply.objects.filter(product_name=product.product_name)
	return render(request, 'rent/list_product.html', {'supplies': supplies, 
	  'product_name': product.product_name})

def delete_product(request, pk):
	if request.method == 'POST':
		if request.POST.get('cancel_button') is not None:
		  return HttpResponseRedirect(reverse('home'))
		else:
		  name_of_product = Supply.objects.get(id=pk).product_name
		  product = Supply.objects.filter(product_name=name_of_product)
		  product.delete()
		  return HttpResponseRedirect(reverse('home'))
	else:
		product = Supply.objects.get(id=pk)
		return render(request, 'rent/confirm_delete_product.html', {'product': product})
		
def delete_index(request, pk):
	if request.method == 'POST':
		if request.POST.get('cancel_button') is not None:
		  return HttpResponseRedirect(reverse('home'))
		else:
		  product = Supply.objects.get(id=pk)
		  product.delete()
		  return HttpResponseRedirect(reverse('home'))
	else:
		product = Supply.objects.get(id=pk)
		return render(request, 'rent/confirm_delete_index.html', {'product': product})
