class linea:
    def __init__(self, string):
        self.word = list(string)
    # replace a char according to the index provided
    def replace_index(self, index, char):
        self.word[index] = char
    # looks for all the old char present and change for new
    def replace_char(self, old, new):
        for index, value in enumerate(self.word):
            if value == old:
                self.word[index] = new
    # appends to the end of the string
    def append(self, string):
        self.word = self.word + list(string)
    # capitalize the first letter
    def capitalize(self):
        self.word[0] = self.word[0].upper()
    # returns the len of the word
    def len(self):
        return len(self.word)
    def upper(self):
        for i, j in enumerate(self.word):
            self.word[i] = j.upper()
        
    def _create_dict(self):
        temp = {}
        for i in self.word:
            if i not in temp:
                temp[i] = 0
        return temp
    # returns a list with the ascii values from each value
    def ascii(self):
        temp = self._create_dict()

        for i in self.word:
            if i in temp:
                temp[i] = ord(i)
        return temp

    def count(self):
        temp = self._create_dict()
        for i in self.word:
            if i in temp:
                temp[i] += 1
        return temp

    def __str__(self):
        return "".join(self.word)

    def __iter__(self):
        self.n = 0
        return self
    def __next__(self):
        if self.n < self.len():
            temp = self.word[self.n]
            self.n += 1
            return temp
        else:
            raise StopIteration
    def __add__(self, other):
        return linea( "".join(self.word)+ str(other))

palabra = linea("antonio")
palabra2 = linea("silva")
palabra3 = linea("paucar")
resultado = palabra + palabra2 + palabra3
print(resultado)

resultado.capitalize()
print(resultado)