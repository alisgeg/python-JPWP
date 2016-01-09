import urllib2
from sys import argv
import os
import time
import urllib

def downloadFlags(listOfCountries):
	for el in listOfCountries:
		print "loading: " + el
		site = "http://www.sciencekids.co.nz/images/pictures/flags680/"
		url = site + el + '.jpg'
		try:
			downloadFlag(url, el)
		except:
			print "unable to download: " + el

def downloadFlag(url, el):
	flag = urllib2.urlopen(url).read()
	tmpFileName = el + '.jpg'
	target = open('./flags/' + tmpFileName, 'w+')
	target.write(flag)

if __name__ == '__main__':
	
	f = open('countryNames.txt', 'r')
	listOfCountries = f.read()
	listOfCountries = listOfCountries.split(' ')
	downloadFlags(listOfCountries)