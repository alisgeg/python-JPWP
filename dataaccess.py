from pymongo import MongoClient

client = MongoClient()
db = client.myDatabase
collection = db['myCollection']
posts = db.posts

def isAlreadyCached(countryName, requestType):
	if posts.find_one({"country": countryName, "requestType": requestType}) != None:
		return True
	else:
		return False

def isFlagAlreadyChecked(url, requestType):
	if posts.find_one({"url": url, "requestType": requestType}) != None:
		return True
	else:
		return False		

def getDocument(countryName, requestType):
	res = posts.find_one({"country": countryName, "requestType": requestType}, {"content": 1})
	return res['content']

def getCountryFromUrl(url, requestType):
	res = posts.find_one({"url": url, "requestType": requestType}, {"country": 1})
	return res['country']

def saveDocument(countryName, requestType, content):
	post = {"country": countryName, "requestType": requestType, "content": content}
	posts.insert_one(post)

def saveUrl(countryName, requestType, url):
	post = {"country": countryName, "requestType": requestType, "url": url}
	posts.insert_one(post)