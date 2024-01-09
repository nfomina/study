from contextlib import contextmanager


@contextmanager
def safe_write(filename):

    new_file = open('test_file.txt', 'w')
    try:
        yield new_file
    except Exception as error:
        print(f"Во время записи в файл было возбуждено исключение {type(error).__name__}")
        return
    else:
        file = open(filename, 'w')
        new_file.close()
        text = open('test_file.txt', 'r')
        file.write(text.read())
        file.close()
    finally:
        new_file.close()


with safe_write('undertale.txt') as file:
    file.write('Тень от руин нависает над вами, наполняя вас решительностью')

with open('undertale.txt') as file:
    print(file.read())

with safe_write('under_tale.txt') as file:
    file.write('Тень от руин нависает над вами, наполняя вас решительностью\n')

with safe_write('under_tale.txt') as file:
    print('Под весёлый шорох листвы вы наполняетесь решительностью', file=file)
    raise ValueError

with open('under_tale.txt') as file:
    print(file.read())
