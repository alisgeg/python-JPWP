import urllib2
from sys import argv
import os
import time
import urllib

def downloadFlags(listOfCountries):
	"""Funkcja, która wywołuje dla każdego kraju z listy funkcję downloadFlag."""

	for el in listOfCountries:
		print "loading: " + el
		site = "http://www.sciencekids.co.nz/images/pictures/flags680/"
		url = site + el + '.jpg'
		try:
			downloadFlag(url, el)
		except:
			print "unable to download: " + el

def downloadFlag(url, el):
	"""Funkcja, która pobiera flagę danego państwa z podanej 
	strony i zapisuje ją w pliku w folderze flags."""

	flag = urllib2.urlopen(url).read()
	tmpFileName = el + '.jpg'
	target = open('./flags/' + tmpFileName, 'w+')
	target.write(flag)

if __name__ == '__main__':
	"""Przy uruchomieniu skryptu wywoływana jest funkcja downloadFlags 
	dla krajów zapisanych w pliku countryNames.txt."""

	f = open('countryNames.txt', 'r')
	listOfCountries = f.read()
	listOfCountries = listOfCountries.split(' ')
	downloadFlags(listOfCountries)