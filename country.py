import urllib2
import nltk
import re
from bs4 import BeautifulSoup
from HTMLParser import HTMLParser
from re import sub
from sys import stderr
from traceback import print_exc
import dataaccess

class _DeHTMLParser(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.__text = []

	def handle_data(self, data):
		text = data.strip()
		if len(text) > 0:
			text = sub('[ \t\r\n]+', ' ', text)
			self.__text.append(text + ' ')

	def handle_starttag(self, tag, attrs):
		if tag == 'p':
			self.__text.append('\n\n')
		elif tag == 'br':
			self.__text.append('\n')

	def handle_startendtag(self, tag, attrs):
		if tag == 'br':
			self.__text.append('\n\n')

	def text(self):
		return ''.join(self.__text).strip()


def dehtml(text):
	try:
		parser = _DeHTMLParser()
		parser.feed(text)
		parser.close()
		return parser.text()
	except:
		print_exc(file=stderr)
		return text


def country(country):
	requestType = "country"
	if dataaccess.isAlreadyCached(country, requestType):
		print "document for " + country + " is already in our database!"
		content = dataaccess.getDocument(country, requestType)
	else:
		print "downloading document for " + country
		site = "https://en.wikipedia.org/wiki/"
		url = site + country
		content = urllib2.urlopen(url).read()
		dataaccess.saveDocument(country, requestType, content)

	soup = BeautifulSoup(content, 'html.parser')


	body = soup.body
	div = soup.body.find('div', id='mw-content-text')
	p = div.find_all('p', recursive = False)


	string = ""
	for el in p:
		if el.find_all('sup') != None:
			for sup in el.find_all('sup'):
				sup.decompose()
		string = string + dehtml(el.__str__())

	string2 = string
	try:
		for pos in xrange(0, len(string)):
			if (string2[pos] == ".") or (string2[pos] == ","):
				if string2[pos-1] == " ":
					string2 = string2[:pos-1] + string2[(pos):]
	except:
		print ''

	return string2

def countryTag(countryName, tag):
	print countryName
	print tag
	string = country(countryName)
	output = ""

	listOfSenteces = string.split(".")
	for sentence in listOfSenteces:
		if sentence.find(tag)>=0:
			output = output + sentence + ". \n"
	
	# while string != "" :
		# if string.find(".")>=0:
			# sentence = string[:string.index(".")+1]
			# if sentence.find(tag)>=0:
			# 	# print "jestem w ifie"
			# 	output = output + sentence + "\n"
			# 	# print output
			# # if string.index(".")+1<len(string):
			# string = string[string.index(".")+1:]
	return output
