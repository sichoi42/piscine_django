from django.shortcuts import render
import psycopg2 as pg2
from django.conf import settings
from django.http import HttpRequest, HttpResponse

# Create your views here.
# setting.DATABASE['default']['']
def init(request: HttpRequest):
	DB = settings.DATABASES['default']
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
			CREATE TABLE IF NOT EXISTS ex00_movies (
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

