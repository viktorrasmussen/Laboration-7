import csv
from PokemonClass import *

class Node():
    """Noder till klassen Hashtable """

    def __init__(self, key="", data=None):
        """key: nyckeln som anvands vid hashningen
        data: det objekt som ska hashas in"""
        self.key = key
        self.data = data

class Hashtable():

    def __init__(self, size):
        """size: hashtabellens storlek"""
        self.size = size
        self.tabell = [None]*int(size)

    def __str__(self):
        return str([i for i in self.tabell])

    def __contains__(self, key):
        return key in self.tabell

    def __getitem__(self, key):
        return self.tabell(key)

    def store(self, key, data):
        """key: nyckeln
           data: objektet som ska lagras
           Stoppar in "data" med nyckeln "key" i tabellen."""
        index = self.hashfunction(key)
        if self.tabell[index] is None: #Lägger till noden om platsen är tom
            self.tabell[index] = Node(key, data)
        else:
            if type(self.tabell[index]) is not list: #Om platsen är upptagen, men inte är en lista, i.e den är upptagen
                if self.tabell[index].key == key: #Om platsen är upptagen med samma key som är aktuell vill vi uppdatera platsen
                    self.tabell[index] = Node(key, data)
                else: #Om platsen är upptagen med ett helt annat objekt vill vi skapa en lista och lägga till noden
                    tmp = Node(key, data)
                    self.tabell[index] = list(self.tabell[index])
                    self.tabell[index].append(tmp)
            else: #Om platsen är upptagen och det redan uppstått en krock tidigare vill vi först se om vi har ett objekt med samma key innan, isf uppdatera datan
                for node in self.tabell[index]:
                    if node.key == key:
                        node.data = data
                    else: #Om nyckeln inte finns sedan innan vill vi lägga till noden i listan
                        self.tabell[index].append(Node(key, data))
    def search(self, key):
        """key: nyckeln
           Hamtar det objekt som finns lagrat med nyckeln "key" och returnerar det.
           Om "key" inte finns ska vi få en Exception, KeyError """
        index = self.hashfunction(key)
        if self.tabell[index] is not None:
            if type(self.tabell[index]) is list: #Om index för nyckeln vi letar efter existerar i en lista linjärsöker vi i denna för att se om objektet finns
                found = False
                for node in self.tabell[index]:
                    if node.key == key:
                        found = True
                        return node.data
                if found is False:
                    raise KeyError(key)
            else:
                node = self.tabell[index]
                if node.key == key:
                    return node.data
                else:
                    raise KeyError(key)

    def hashfunction(self, key):
        """key: nyckeln
        Beräknar hashfunktionen för key"""
        if type(key) is str:
            tmp = list(key)
            key_letters = [str(ord(letter)) for letter in tmp] #Gör om nyckelns bokstäver till siffror i en sträng
            key_integers = int(''.join(key_letters))**3 #Gör om sträng-siffrorna till integers för att kunna höja upp till 3
            tmp2 = list(str(key_integers)) #Återgår till att ha nyckeln som sträng-siffror, ett element per siffra
            length = len(tmp2)//2
            hashable_key = ""
            for i in range(-2, 2):
                hashable_key = (hashable_key + tmp2[length + i])

        hashable_key = int(hashable_key) % self.size
        index = list(hashable_key)
        index.append(hashable_key)
        return index


def read_file(file):
    nodes = list()
    with open(file, 'r', encoding="utf-8") as pokemon_file:
        for pokemon in pokemon_file:
            temp = pokemon.split(',')
            temp2 = Pokemon(temp[1], temp[2], temp[3], temp[4], temp[5], temp[6], temp[7], temp[8], temp[9], temp[10],
                            temp[11], temp[12])
            node = Node(temp2.name, temp2)
            nodes.append(node)
    return nodes

a = read_file('pokemon.csv')

b = Hashtable(10000)

print(a)

#for i in a:
#   b.store(i.key, i.data)

#print(a)

#print(type(b.hashfunction('Turtle')))

#print(b)


