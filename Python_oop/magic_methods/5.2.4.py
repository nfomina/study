from functools import singledispatchmethod


class IPAddress:
    @singledispatchmethod
    def __init__(self, ipaddress):
        self.ipaddress = ''

    @singledispatchmethod
    @__init__.register(str)
    def from_str(self, ipaddress):
        self.ipaddress = ipaddress

    @singledispatchmethod
    @__init__.register(list)
    @__init__.register(tuple)
    def from_list_tuple(self, ipaddress):
        self.ipaddress = '.'.join(map(str, ipaddress))

    def __str__(self):
        return self.ipaddress

    def __repr__(self):
        return f"IPAddress('{self.ipaddress}')"


ip = IPAddress('8.8.1.1')

print(str(ip))
print(repr(ip))

ip = IPAddress([1, 1, 10, 10])

print(str(ip))
print(repr(ip))

ip = IPAddress((1, 1, 11, 11))

print(str(ip))
print(repr(ip))
