class Greeter:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print(f'Приветствую, {self.name}!')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print(f'До встречи, {self.name}!')
        return True


with Greeter('Кейв'):
    print('...')

with Greeter('Кейв') as greeter:
    print(greeter.name)

with Greeter('Матильда') as greeter:
    pass

with Greeter('Михаил Г.') as greeter:
    print(
        '\nКак бессонница в час ночной\n'
        'Меняет, нелюдимая, облик твой,\n'
        'Чьих невольница ты идей?\n'
        'Зачем тебе охотиться на людей?\n'
    )