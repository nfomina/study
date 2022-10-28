import pickle


def filter_dump(filename, objects, typename):
    with open(filename, 'wb') as file:
        pickle.dump(list(filter(lambda x: type(x) == typename, objects)), file)





filter_dump('numbers.pkl', [1, '2', 3, 4, '5'], int)
# должен создавать файл numbers.pkl, содержащий сериализованный список [1, 3, 4].