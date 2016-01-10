# This Python file uses the following encoding: utf-8
import requests
import json
from subprocess import call, check_call

numberOfPort = 0

if __name__ == '__main__':
	"""Uruchomienie tego skryptu powoduje wysłanie do serwera JSONa złożonego z treści pobranej od użytkownika."""

	print "Which information do you need? Choose one option (type a number):"
	print "1) All information about country."
	print "2) Specific information about country."
	print "3) Checking country based on flag."
	print "4) Reciving flag of specific country."
	option = int(raw_input("I choose number: "))

	if option == 1:
		countryName = raw_input("Type a name of country: ")
		content = "country(" + countryName + ")"
		typeOfQuestion = 'text'

	elif option == 2:
		countryName = raw_input("Type a name of country: ")
		countryTag = raw_input("Type key word: ")
		content = "country(" + countryName + ");tag(" + countryTag + ")"
		typeOfQuestion = 'text'

	elif option == 3:
		linkToFlag = raw_input("Paste a link to flag (in .jpg or .png format): ")
		content = "checkflag(" + linkToFlag + ")"
		typeOfQuestion = 'image'

	elif option == 4:
		countryName = raw_input("Type a name of country whose flag you want: ")
		content = "country(" + countryName + ");getflag"
		typeOfQuestion = 'image'

	else:
		print "Invalid data."


	payload = {'address': '', 'port': numberOfPort, 'type': typeOfQuestion, 'content': content}
	
	r = requests.post("http://localhost:8009", params = json.dumps(payload))
	print r.text