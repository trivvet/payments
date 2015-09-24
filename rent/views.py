# -*- coding: utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from .models import Supply
import pdb

# Create your views here.

def home(request):
	if Supply.objects.count() > 0:
		supplies = Supply.objects.order_by('product_name')
		return render(request, 'rent/home.html', {'supplies': supplies})
	else: 
		return render(request, 'rent/home.html', {})
	
def add_product(request):
	if request.method == 'POST':
		if request.POST.get('cancel_button') is not None:
		  return HttpResponseRedirect(reverse('home'))
		elif request.POST.get('add_button') is not None:
		  data = {}
		  name_of_product = {
		    'water': u'Водопостачання',
		    'sewerage': u'Каналізація',
		    'electricity': u'Електропостачання',
		    'gas': u'Газопостачання',
		    'waste': u'Вивіз сміття'
		  }
		  data['product_name'] = name_of_product[request.POST.get('product_name', '').strip()]
		  data['provider_name'] = request.POST.get('provider_name', '').strip()
		  provider_site = request.POST.get('provider_site', '').strip()
		  data['provider_site'] = 'http://' + provider_site
		  for i in range(1,5):
			  counter_name = request.POST.get('counter_' + str(i) + '_name')
			  counter_indicator = request.POST.get('counter_' + str(i) + '_indicator')
			  print counter_name, counter_indicator
			  if len(counter_name) > 0 and len(counter_indicator) > 0:
				  data['counter_' + str(i) + '_name'] = counter_name
				  data['counter_' + str(i) + '_indicator'] = int(counter_indicator)
		  data['arrears'] = request.POST.get('arrears', '').strip()
		  product = Supply(**data)
		  product.save()
		  return HttpResponseRedirect(reverse('home'))
	else:
		return render(request, 'rent/add_product.html', {})
		
def edit_indexes(request, pk):
	if request.method == 'POST':
		if request.POST.get('cancel_button') is not None:
		  return HttpResponseRedirect(reverse('home'))
		elif request.POST.get('save_button') is not None:
		  supply = Supply.objects.get(id=pk)
		  data = {}
		  data['product_name'] = supply.product_name
		  data['provider_name'] = supply.provider_name
		  data['provider_site'] = supply.provider_site
		  for i in range(1,5):
			  counter_name_number = 'counter_' + str(i) + '_name'
			  exec('counter_name = supply.counter_%s_name' % i)
			  counter_indicator = request.POST.get('counter_' + str(i) + '_indicator')
			  print counter_name, counter_indicator
			  if len(counter_name) > 0 and len(counter_indicator) > 0:
				  data['counter_' + str(i) + '_name'] = counter_name
				  data['counter_' + str(i) + '_indicator'] = int(counter_indicator)
		  data['arrears'] = request.POST.get('arrears', '').strip()
		  product = Supply(**data)
		  product.save()
		  return HttpResponseRedirect(reverse('home'))
	else:
		supply = Supply.objects.get(id=pk)
		return render(request, 'rent/edit_indexes.html', {'supply': supply})
		
def delete_product(request, pk):
	if request.method == 'POST':
		if request.POST.get('cancel_button') is not None:
		  return HttpResponseRedirect(reverse('home'))
		else:
		  product = Supply.objects.get(id=pk)
		  product.delete()
		  return HttpResponseRedirect(reverse('home'))
	else:
		product = Supply.objects.get(id=pk)
		return render(request, 'rent/confirm_delete_product.html', {'product': product})
