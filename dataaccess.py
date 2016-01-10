# This Python file uses the following encoding: utf-8
from pymongo import MongoClient

client = MongoClient()
db = client.myDatabase
collection = db['myCollection']
posts = db.posts

def isAlreadyCached(countryName, requestType):
	"""Funkcja, która sprawdza, czy odpowiedź na zapytanie typu country(country_name) znajduje się w bazie."""

	if posts.find_one({"country": countryName, "requestType": requestType}) != None:
		return True
	else:
		return False

def isFlagAlreadyChecked(url, requestType):
	"""Funkcja, która sprawdza, czy odpowiedź na zapytanie typu checkflag(url) znajduje się w bazie."""

	if posts.find_one({"url": url, "requestType": requestType}) != None:
		return True
	else:
		return False		

def getDocument(countryName, requestType):
	"""Funkcja, która pobiera treść odpowiedzi na zapytanie country(country_name) z bazy."""

	res = posts.find_one({"country": countryName, "requestType": requestType}, {"content": 1})
	return res['content']

def getCountryFromUrl(url, requestType):
	"""Funkcja, która pobiera treść odpowiedzi na zapytanie checkflag(url) z bazy."""

	res = posts.find_one({"url": url, "requestType": requestType}, {"country": 1})
	return res['country']

def saveDocument(countryName, requestType, content):
	"""Funkcja, która zapisuje odpowiedź na treśc zapytania typu country(country_name) do bazy."""

	post = {"country": countryName, "requestType": requestType, "content": content}
	posts.insert_one(post)

def saveUrl(countryName, requestType, url):
	"""Funkacja, która zapisuje odpowiedź na treść zapytania typu checkflag(url) do bazy."""

	post = {"country": countryName, "requestType": requestType, "url": url}
	posts.insert_one(post)