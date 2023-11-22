class Ord:
    def __getattribute__(self, name):
        return ord(name)


obj = Ord()

print(obj.a)
print(obj.b)

obj = Ord()

print(obj.в)
print(obj.г)

# TEST_3:
obj = Ord()
chars = ['|', 'j', 'S', 'g', 'v', 'Y', 'L', 'z', 'a', '3', 'p', '\\', '>', "'", '_', 'I', '!', '=', '#', '(', 'U', 'J',
         'h', 't', '`', '{', 'B', '\n', '&', 'P', 'e', '[', 'i', 'E', 'f', '8', 'V', ':', 'O', 'o', '$', ')', 'l', 'W',
         ';', '^', 'K', '?', '7', '}', 'q', ']', 'M', 'C', '9', 'c', 'T', '*', 'y', 's', '\r', '2', 'k', '-', 'Z', '.',
         '\t', 'D', '\x0c', '@', '"', '~', '6', '0', ' ', '1', 'b', 'R', '4', 'Q', 'r', 'G', '5', 'u', 'N', '+', 'd',
         'F', 'x', 'A', '<', '/', '%', 'm', ',', 'n', '\x0b', 'X', 'H', 'w']

for char in chars:
    print(getattr(obj, char))
