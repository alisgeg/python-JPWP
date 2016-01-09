#opis

Aby uruchomić aplikację należy:
-utworzyć folder /flags w miejscu, gdzie znajduje się reszta plików,
-pobrać flagi za pomocą skryptu:
	python downloadFlags.py
-uruchomić serwer (wystartuje on na porcie 8009):
	python server.py
-gdy serwer wystartuje należy uruchomić skrypt klienta:
	python client.py
i postępować zgodnie ze wskazówkami:
1-country(country_name)
2-country(country_name);tag(tag)
3-country(country_name);getflag
4-getflag(country_name)

Aby uruchomić testy podobne do tych wcześniej udostępnionych należy włączyć serwer testowy i podać port 8009.


