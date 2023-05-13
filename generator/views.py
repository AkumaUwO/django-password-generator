from django.shortcuts import render
import random
#from django.http import HttpResponse

# Create your views here.
def about(request):
	return render(request, 'generator/about.html')

def home(request):
	return render(request, 'generator/home.html')

def password(request):
	# Declaración de Variables
	characters = list('abcdefghijklmnopqrstuvwxyz')
	generated_password = ''
	length = int(request.GET.get('length'))

	#Si se marca el checkbox mayusculas, usar mayusculas


	if request.GET.get('uppercase'):
		characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

	if request.GET.get('special'):
		characters.extend(list('$%&?!#@*'))

	if request.GET.get('number'):
		characters.extend(list('0123456789'))	

	for x in range(length):
		generated_password += random.choice(characters)

	return render(request, 'generator/password.html', {'password': generated_password})