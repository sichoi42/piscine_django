from django.shortcuts import render, redirect
import psycopg2 as pg2
from django.conf import settings
from django.http import HttpRequest, HttpResponse
from .forms import Remove

# Create your views here.
# setting.DATABASE['default']['']
DB = settings.DATABASES['default']

def init(request: HttpRequest):
	try:
		conn = pg2.connect(
			host='localhost',
			dbname=DB['NAME'],
			user=DB['USER'],
			password=DB['PASSWORD'],
			port=5432
		)
		cur = conn.cursor()
		cur.execute("""
			CREATE TABLE IF NOT EXISTS ex04_movies (
			title VARCHAR(64) UNIQUE NOT NULL,
			episode_nb INT PRIMARY KEY,
			opening_crawl TEXT,
			director VARCHAR(32) NOT NULL,
			producer VARCHAR(128) NOT NULL,
			release_date DATE NOT NULL
			);
			""")
		conn.commit()
		cur.close()
		conn.close()
		return HttpResponse('OK')
	except Exception as e:
		return HttpResponse(e)

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
	try:
		conn = pg2.connect(
			host='localhost',
			dbname=DB['NAME'],
			user=DB['USER'],
			password=DB['PASSWORD'],
			port=5432
		)
		cur = conn.cursor()
		for movie in movies:
			cur.execute("""
				INSERT INTO ex04_movies (
					title, episode_nb, director, producer, release_date
				) VALUES (
				'{0}', '{1}', '{2}', '{3}', '{4}'
				);
				""".format(
					movie['title'],
					movie['episode_nb'],
					movie['director'],
					movie['producer'],
					movie['release_date'],
				))
		conn.commit()
		cur.close()
		conn.close()
		return HttpResponse('OK')
	except Exception as e:
		return HttpResponse(e)

def display(request: HttpRequest):
	try:
		conn = pg2.connect(
			host='localhost',
			dbname=DB['NAME'],
			user=DB['USER'],
			password=DB['PASSWORD'],
			port=5432
		)
		cur = conn.cursor()
		cur.execute("SELECT * FROM ex04_movies")
		movies = cur.fetchall()
		cur.close()
		conn.close()
		return render(request, 'display3.html', {'movies': movies})
	except:
		return HttpResponse('No data available')

def remove(request: HttpRequest):
	try:
		conn = pg2.connect(
			host='localhost',
			dbname=DB['NAME'],
			user=DB['USER'],
			password=DB['PASSWORD'],
			port=5432
		)
		cur = conn.cursor()
		cur.execute("SELECT title from ex04_movies")
		titles = cur.fetchall()
		choices = []
		for title in titles:
			choices.append((title[0], title[0]))
		data = Remove(choices, request.POST)
		if data.is_valid() == True:
			cur.execute("""
			DELETE FROM ex04_movies WHERE title='{0}'
			""".format(data.cleaned_data['title']))
			conn.commit()
			return redirect('/ex04/remove')
		return render(request, 'remove.html', {'data': Remove(choices)})
	except:
		return HttpResponse('No data available')

