class generateDictionary :

    def init(self, keys, maps) :
        self.keys = keys
        self.maps = maps

    def generate(self) :
        dictionary = {}
        for i in range(len(self.maps)):
            dictionary[self.keys[i]] = self.maps[i]
        return dictionary



