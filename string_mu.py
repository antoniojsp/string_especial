class strm:
    def __init__(self, string):
        self.temp = list(string)
    def replace(self, index, char):
        self.temp[index] = char
    def append(self, string):
        self.temp = self.temp + list(string)
    def capitalize(self):
        self.temp[0] = self.temp[0].upper()
    def len(self):
        return len(self.temp)

    def __str__(self):
        return "".join(self.temp)



string = strm("hola")
print(string)

string.replace(1, "A")
print(string)

string.append(" Antonio")
print(string)

string.capitalize()
print(string)

print(string.len())
print(string)
