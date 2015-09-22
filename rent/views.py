from django.shortcuts import render
from .models import Supply

# Create your views here.

def home(request):
	supplies = Supply.objects.all()
	
	return render(request, 'rent/home.html', {'supplies': supplies})
