class strm:
    def __init__(self, string):
        self.temp = list(string)
    # replace a char according to the index provided
    def replace_index(self, index, char):
        self.temp[index] = char
    # looks for all the old char present and change for new
    def replace_char(self, old, new):
        for index, value in enumerate(self.temp):
            if value == old:
                self.temp[index] = new
            else:
                pass
    # appends to the end of the string
    def append(self, string):
        self.temp = self.temp + list(string)
    # capitalize the first letter
    def capitalize(self):
        self.temp[0] = self.temp[0].upper()
    # returns the len of the word
    def len(self):
        return len(self.temp)
    # returns a list with the ascii values from each value
    def ascii(self):
        values = []
        for i in self.temp:
            values.append(ord(i))
        return values
    # return a dictionary with all incidences
    def count(self):
        temp = {}
        for i in self.temp:
            if i in temp:
                temp[i] += 1
            else:
                temp[i] = 1
        return temp

    def __str__(self):
        return "".join(self.temp)
    def __iter__(self):
        self.n = 0
        return self
    def __next__(self):
        if self.n < self.len():
            temp = self.temp[self.n]
            self.n += 1
            return temp
        else:
            raise StopIteration

string = strm("aaaaa")
print(string)
string.replace_char("h", "L")
print(string)
print(string.count())
