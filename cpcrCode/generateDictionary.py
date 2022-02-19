
from markupsafe import Markup


class generateDictionary :

    def __init__(self) :
        self.book = dict()

    def generate(self, keys, maps) :
        for i in range(len(maps)):
            self.addEntry(keys[i], maps[i])

    def addEntry(self, key, map) :
        if map in self.book :
            print("map already in dictionary")
        else:
            self.book[key] = map

    def returnDictionary(self) :
        return self.book