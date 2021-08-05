from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Movies
from .forms import Update

# Create your views here.

def populate(request: HttpRequest):
	movies = [
		{
			'episode_nb': '1',
			'title': 'The Phantom Menace',
			'director': 'George Lucas',
			'producer': 'Rick McCallum',
			'release_date': '1999-05-19'
		},
		{
			'episode_nb': '2',
			'title': 'Attack of the Clones',
			'director': 'George Lucas',
			'producer': 'Rick McCallum',
			'release_date': '2002-05-16'
		},
		{
			'episode_nb': '3',
			'title': 'Revenge of the Sith',
			'director': 'George Lucas',
			'producer': 'Rick McCallum',
			'release_date': '2005-05-19'
		},
		{
			'episode_nb': '4',
			'title': 'A New Hope',
			'director': 'George Lucas',
			'producer': ' Gary Kurtz, Rick McCallum',
			'release_date': '1977-05-25'
		},
		{
			'episode_nb': '5',
			'title': 'The Empire Strikes Back',
			'director': 'Irvin Kershner',
			'producer': 'Gary Kurtz, Rick McCallum',
			'release_date': '1980-05-17'
		},
		{
			'episode_nb': '6',
			'title': 'Return of the Jedi',
			'director': 'Richard Marquand',
			'producer': 'Howard G. Kazanjian, George Lucas, Rick McCallum',
			'release_date': '1983-05-25'
		},
		{
			'episode_nb': '7',
			'title': 'The Force Awakens',
			'director': 'J. J. Abrams',
			'producer': 'Kathleen Kennedy, J. J. Abrams, Bryan Burk',
			'release_date': '2015-12-11'
		}
	]
	for data in movies:
		try:
			Movies.objects.create(
				title=data['title'],
				episode_nb=data['episode_nb'],
				director=data['director'],
				producer=data['producer'],
				release_date=data['release_date'],
			)
		except Exception as e:
			return HttpResponse(e)
	return HttpResponse('OK')

def display(request: HttpRequest):
	try:
		movies = Movies.objects.all()
		return render(request, 'display6.html', {'movies': movies})
	except Exception:
		return HttpResponse('No data available')

def update(request: HttpRequest):
	try:
		movies = Movies.objects.all()
		choices = []
		print(1)
		for movie in movies:
			choices.append((movie.title, movie.title))
		data = Update(choices, request.POST)
		if data.is_valid() == True:
			new = Movies.objects.get(title=data.cleaned_data['title'])
			new.opening_crawl = data.cleaned_data['opening_crawl']
			new.save()
			return redirect('/ex07/update')
		return render(request, 'update2.html', {'data': Update(choices)})
	except:
		return HttpResponse('No data available')
