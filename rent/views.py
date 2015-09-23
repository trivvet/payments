# -*- coding: utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from .models import Supply
import pdb

# Create your views here.

def home(request):
	if Supply.objects.count() > 0:
		supplies = Supply.objects.all()
		return render(request, 'rent/home.html', {'supplies': supplies})
	else: 
		return render(request, 'rent/home.html', {})
	
	return render(request, 'rent/home.html', {'supplies': supplies})
	
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
		  data['arrears'] = request.POST.get('arrears', '').strip()
		  product = Supply(**data)
		  product.save()
		  return HttpResponseRedirect(reverse('home'))
	else:
		return render(request, 'rent/add_product.html', {})
		
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
