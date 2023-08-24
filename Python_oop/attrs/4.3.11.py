class Postman:
    def __init__(self):
        self.delivery_data = []

    def add_delivery(self, street, house, flat):
        self.delivery_data.append((street, house, flat))

    def get_houses_for_street(self, street):
        res = []
        for item in [item[1] for item in filter(lambda a: a[0] == street, self.delivery_data)]:
            if item not in res:
                res.append(item)
        return res

    def get_flats_for_house(self, street, house):
        res = []
        for item in [item[2] for item in filter(lambda a: a[0] == street and a[1] == house, self.delivery_data)]:
            if item not in res:
                res.append(item)
        return res


postman = Postman()

print(postman.delivery_data)
print(postman.get_houses_for_street('3-я ул. Строителей'))
print(postman.get_flats_for_house('3-я ул. Строителей', 25))

postman = Postman()

postman.add_delivery('Советская', 151, 74)
postman.add_delivery('Советская', 151, 75)
postman.add_delivery('Советская', 90, 2)
postman.add_delivery('Советская', 151, 74)

print(postman.get_houses_for_street('Советская'))
print(postman.get_flats_for_house('Советская', 151))
