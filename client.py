import requests
import json
from subprocess import call, check_call

numberOfPort = 0

if __name__ == '__main__':
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
		linkToFlag = raw_input("Paste a link to flag (in .jpg format): ")
		content = "checkflag(" + linkToFlag + ")"
		typeOfQuestion = 'image'

	elif option == 4:
		countryName = raw_input("Type a name of country whose flag you want: ")
		content = "country(" + countryName + ");getflag"
		typeOfQuestion = 'image'


	else:
		print "Invalid data."


	payload = {'address': '', 'port': numberOfPort, 'type': typeOfQuestion, 'content': content}
	# payload = payload.decode('utf8', 'ignore')
	# check_call(["curl", "-H", "\"Content-Type:application/json\"", "--data", json.dumps(payload), "-X", "POST", "http://httpbin.org/", "--local-port", numberOfPort])
	# curl -H "Content-Type:application/json" --data "{checkflag(http://www.flagpictures.org/downloads/print/slovenia1.jpg)}" -X POST localhost:8009 --local-port RANGE

	r = requests.post("http://localhost:8009", params = json.dumps(payload))
	print r.text