from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Planets, People
import json
#from .forms import Update
# Create your views here.

def populate(request: HttpResponse):
	try:
		with open('./ex09_initial_data.json','r') as f:
			data = json.load(f)
			i = 0
			while data[i]['model'] == 'ex09.planets':
				Planets.objects.create(
					name=data[i]['fields']['name'],
					climate=data[i]['fields']['climate'],
					diameter=data[i]['fields']['diameter'],
					orbital_period=data[i]['fields']['orbital_period'],
					population=data[i]['fields']['population'],
					rotation_period=data[i]['fields']['rotation_period'],
					surface_water=data[i]['fields']['surface_water'],
					terrain=data[i]['fields']['terrain']
				)
				i = i + 1
				j = i
			while i < j + 87:
				People.objects.create(
					name=data[i]['fields']['name'],
					birth_year=data[i]['fields']['birth_year'],
					gender=data[i]['fields']['gender'],
					eye_color=data[i]['fields']['eye_color'],
					hair_color=data[i]['fields']['hair_color'],
					height=data[i]['fields']['height'],
					mass=data[i]['fields']['mass'],
					homeworld=data[i]['fields']['homeworld']
				)
				i = i + 1
		return HttpResponse('OK')
	except Exception as e:
			return HttpResponse(e)

# def display(request: HttpRequest):
	# try:
	# 	movies = Movies.objects.all()
	# 	return render(request, 'display6.html', {'movies': movies})
	# except Exception:
	# 	return HttpResponse('No data available')
