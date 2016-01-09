import country as count
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import os
import time
import re
import urllib2
from myimage import compare
import requests
import json
from sys import argv
import sys  
import dataaccess
 
 
reload(sys)  
sys.setdefaultencoding('utf8')
 
HOST_NAME = "localhost"
PORT_NUMBER = 8009
 
def respond(self, content, address = "", port = 0):
    """Funkcja, która wysyła odpowiedź na wysłany w JSONie adres. 
    W przypadku pierwszym jest to odpowiedź na generowane przez skrypt client.py zapytanie."""

    if address == "" and port == 0:
        self.send_response(200)
        self.send_header('Content-type','text-html')
        self.end_headers()
        self.wfile.write(content)
    else:
        self.send_response(200)
        self.end_headers()
        headers = {'content-type': 'text/plain'}
        requests.post("http://%s:%s" % (address, port), params = content[:2048], data=content, headers=headers)
 
 
class CountriesHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        """Reakcja serwera na otyrzymaną metodę POST.
        Pobierana jest treść zapytania, a następnie porównywana jest ona z odpowiednimi
        wyrażeniami regularnymi, w celu zidentyfikowania typu zapytania.
        W zależności od typu zapytania wywoływane są odpowiednie funkcje
        lub treść pobierana jest z bazy danych. Potem wynik wysyłany jest 
        za pomocą metody respond."""
 
        # country = "Poland"
        filename = argv
 
        length = int(self.headers['Content-Length'])
        data = self.rfile.read(length)
        if self.path != "/":
            data = self.path[2:]
            data = data.replace('%20', ' ')
            data = data.replace('%22', '\"')
            data = data.replace('%7B', '{')
            data = data.replace('%7D', '}')
        data = json.loads(data)
        requestContent = data["content"]
        requestContent = requestContent.decode('utf8', 'ignore')
        print requestContent
 
        address = data["address"]
        port = int(data["port"])
 
        patternCountry = re.compile("country\([A-Z][a-z]*\s?[A-Z]?[a-z]*\)$")
        patternCountryTag = re.compile("country\([A-Z][a-z]*\s?[A-Z]?[a-z]*\)\;tag\(.*\)$")
        patternGetflag = re.compile("country\([A-Z][a-z]*\s?[A-Z]?[a-z]*\)\;getflag$")
        patternCheckflag = re.compile("checkflag\(https?\:.*\)$")
 
        if re.match(patternCountry, requestContent):
            requestContent = requestContent.replace(' ', '_')
            country1 = requestContent[requestContent.index("(")+1:requestContent.index(")")]
            respond(self, count.country(country1), address, port)
 
        elif re.match(patternCountryTag, requestContent):
            requestContent = requestContent.replace(' ', '_')
            country1 = requestContent[requestContent.index("(")+1:requestContent.index(")")]
            tag = requestContent[requestContent.index(";")+1:]
            tag = tag[tag.index("(")+1:tag.index(")")]
            respond(self, count.countryTag(country1, tag), address, port)
 
        elif re.match(patternCheckflag, requestContent):
            requestType = "checkingFlag"
            url = requestContent[requestContent.index("(")+1:requestContent.index(")")]
 
            if dataaccess.isFlagAlreadyChecked(url, requestType):
                tmp = dataaccess.getCountryFromUrl(url, requestType)
                response_content = tmp
            else:
                country = cacheAndResolveCountryName(str(url))
                country = country[:-4]
                response_content = country
                respond(self, response_content, address, port)
 
        elif re.match(patternGetflag, requestContent):
            requestContent = requestContent.replace(' ', '_')
            countryName = requestContent[requestContent.index("(")+1:requestContent.index(")")]
            countryName.lower().capitalize() 
            url = "http://www.sciencekids.co.nz/images/pictures/flags680/" + countryName + ".jpg"
            respond(self, url, address, port)
 
 
def cacheAndResolveCountryName(url):
    """Funkcja wykorzystywana w zapytaniu typu checkflag(url).
    Tworzy (lub nadpisuje) plik, w którym zapisuje pobraną z urla flagę.
    Potem wywołuje funkcję myimage.compare."""

    import urllib2
    from myimage import compare
    extension = url[-3:]
    image = urllib2.urlopen(url).read()
    tmpFileName = 'test.' + extension
    with open(tmpFileName, 'w+') as f:
        f.write(image)
    resName = compare(tmpFileName)
    return resName
 
if __name__ == '__main__':
    """Włączenie serwera."""

    server_class = HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), CountriesHandler)
    print time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER)