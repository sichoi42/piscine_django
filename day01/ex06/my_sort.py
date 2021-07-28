def sort_dict():
	d = {
		'Hendrix' : '1942',
		'Allman' : '1946',
		'King' : '1925',
		'Clapton' : '1945',
		'Johnson' : '1911',
		'Berry' : '1926',
		'Vaughan' : '1954',
		'Cooder' : '1947',
		'Page' : '1944',
		'Richards' : '1943',
		'Hammett' : '1962',
		'Cobain' : '1967',
		'Garcia' : '1942',
		'Beck' : '1944',
		'Santana' : '1947',
		'Ramone' : '1948',
		'White' : '1975',
		'Frusciante': '1970',
		'Thompson' : '1949',
		'Burton' : '1939',
	}
	sort_d = sorted(d.items(), key = lambda x : x[1])
	for i in range(1, len(sort_d)):
		if sort_d[i - 1][1] == sort_d[i][1]:
			if sort_d[i - 1][0] > sort_d[i][0]:
				tmp = sort_d[i - 1]
				sort_d[i - 1] = sort_d[i]
				sort_d[i] = tmp
	sort_d = dict(sort_d)
	for key in sort_d.keys():
		print(key)

if __name__ == '__main__':
	sort_dict()
