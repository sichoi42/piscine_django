from django.shortcuts import render, redirect
import psycopg2 as pg2
from django.conf import settings
from django.http import HttpRequest, HttpResponse

# Create your views here.
# setting.DATABASE['default']['']
DB = settings.DATABASES['default']
table1 = 'ex08_planets'
table2 = 'ex08_people'

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
		CREATE TABLE IF NOT EXISTS ex08_planets (
		id SERIAL PRIMARY KEY,
		name VARCHAR(64) UNIQUE NOT NULL,
		climate VARCHAR,
		diameter INT,
		orbital_period INT,
		population BIGINT,
		rotation_period INT,
		surface_water REAL,
		terrain VARCHAR(128)
		)
		""")
		cur.execute("""
		CREATE TABLE IF NOT EXISTS ex08_people (
		id SERIAL PRIMARY KEY,
		name VARCHAR(64) UNIQUE NOT NULL,
		birth_year VARCHAR(32),
		gender VARCHAR(32),
		eye_color VARCHAR(32),
		hair_color VARCHAR(32),
		height INT,
		mass REAL,
		homeworld VARCHAR(64) REFERENCES ex08_planets(name)
		)
		""")
		conn.commit()
		cur.close()
		conn.close()
		return HttpResponse('OK')
	except Exception as e:
		return HttpResponse(e)

def read_planets(line):
	line = line.split('\t')
	planet = {
		'name': line[0] if line[0] != 'NULL' else None,
		'climate': line[1] if line[1] != 'NULL' else None,
		'diameter': line[2] if line[2] != 'NULL' else None,
		'orbital_period': line[3] if line[3] != 'NULL' else None,
		'population': line[4] if line[4] != 'NULL' else None,
		'rotation_period': line[5] if line[5] != 'NULL' else None,
		'surface_water': line[6] if line[6] != 'NULL' else None,
		'terrain': line[7].strip('\n') if line[7].strip('\n') != 'NULL' else None
	}
	return planet

def read_peoples(line):
	line = line.split('\t')
	people = {
		'name': line[0] if line[0] != 'NULL' else None,
		'birth_year': line[1] if line[1] != 'NULL' else None,
		'gender': line[2] if line[2] != 'NULL' else None,
		'eye_color': line[3] if line[3] != 'NULL' else None,
		'hair_color': line[4] if line[4] != 'NULL' else None,
		'height': line[5] if line[5] != 'NULL' else None,
		'mass': line[6] if line[6] != 'NULL' else None,
		'homeworld': line[7].strip('\n') if line[7].strip('\n') != 'NULL' else None
	}
	return people

def populate(request: HttpRequest):
	try:
		with open("./planets.csv", 'r') as f1:
			planets = [read_planets(line) for line in f1.readlines()]
		with open("./people.csv", 'r') as f1:
			peoples = [read_peoples(line) for line in f1.readlines()]
		conn = pg2.connect(
				host='localhost',
				dbname=DB['NAME'],
				user=DB['USER'],
				password=DB['PASSWORD'],
				port=5432
			)
		cur = conn.cursor()
		print(planets)
		for planet in planets:
			cur.execute("""
				INSERT INTO ex08_planets (
				name, climate, diameter, orbital_period,
				population, rotation_period, surface_water, terrain
				) VALUES (
				%s, %s, %s, %s, %s, %s, %s, %s
				);
				""",
				[
					planet['name'],
					planet['climate'],
					planet['diameter'],
					planet['orbital_period'],
					planet['population'],
					planet['rotation_period'],
					planet['surface_water'],
					planet['terrain']
				]
				)
		for people in peoples:
			cur.execute("""
				INSERT INTO ex08_people (
				name, birth_year, gender, eye_color,
				hair_color, height, mass, homeworld
				) VALUES (
				%s, %s, %s, %s, %s, %s, %s, %s
				);
				""",
				[
					people['name'],
					people['birth_year'],
					people['gender'],
					people['eye_color'],
					people['hair_color'],
					people['height'],
					people['mass'],
					people['homeworld']
				]
				)
		conn.commit()
		cur.close()
		conn.close()
		return HttpResponse('OK')
	except:
		return HttpResponse('No data available')

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
		cur.execute("""
		SELECT ex08_people.name, ex08_people.homeworld, ex08_planets.climate
		FROM ex08_people LEFT JOIN ex08_planets
		ON ex08_people.homeworld = ex08_planets.name
		WHERE ex08_planets.climate LIKE '%windy%'
		ORDER BY ex08_people.name ASC;
		""")
		results = cur.fetchall()
		print(results)
		cur.close()
		conn.close()
		return render(request, 'display7.html', {'results': results})
	except Exception as e:
		return HttpResponse(e)
