# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render
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
		return HttpResponse(u'<h2>Форма додавання послуги<h2>')
	else:
		return render(request, 'rent/add_product.html', {})
