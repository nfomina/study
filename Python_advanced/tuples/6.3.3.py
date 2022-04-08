poet_data = ('Пушкин', 1799, 'Санкт-Петербург')
list_poet_data = list(poet_data)
list_poet_data[2] = 'Москва'
poet_data = tuple(list_poet_data)
print(poet_data)