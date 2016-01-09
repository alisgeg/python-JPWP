import imread.imread as superimread

def read(filename):
	"""Funkcja umieszczona jest w osobnym skrypcie z powodu generowania dużej ilości błędów 
	wynikających najprawdopodobniej z "mieszania" się bibliotek, które nie ustawały nawet 
	przy dokładnym opisywaniu pochodzenia każdej funkcji."""
	return superimread(filename)