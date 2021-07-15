class strm:
    def __init__(self, string):
        self.temp = list(string)
    def replace(self, index, char):
        self.temp[index] = char
    def append(self, string):
        self.temp = self.temp + list(string)
    def capitalize(self):
        self.temp[0] = self.temp[0].upper()
    def str(self):
        return "".join(self.temp)
    def len(self):
        return len(self.temp)


string = strm("hola")
print(string.str())

string.replace(1, "A")
print(string.str())

string.append("Antonio")
print(string.str())

string.capitalize()
print(string.str())

print(string.len())
