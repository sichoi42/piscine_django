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

if __name__=='__main__':
	with open("../planets.csv", 'r') as f1:
		planets = [read_planets(line) for line in f1.readlines()]
	print(planets)
