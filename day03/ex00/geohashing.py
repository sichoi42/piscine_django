#!/usr/bin/python3
import sys
import antigravity

def geohashing():
	if len(sys.argv) == 4:
		try:
			latitude = float(sys.argv[1])
		except:
			print('please give correct latitude')
		try:
			longtitude = float(sys.argv[2])
		except:
			print('please give correct longtitude')
		day_dowtime = sys.argv[3].encode('utf-8')
		antigravity.geohash(latitude, longtitude, day_dowtime)
	else:
		print('You should give 3 parameters, latitude longtitude day_dowtime')

if __name__ == '__main__':
	geohashing()
