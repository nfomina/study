class HtmlTag:
    tags = []

    def __init__(self, tag, inline=False):
        self.open_tag = f'<{tag}>'
        self.close_tag = f'</{tag}>'
        self.inline = inline
        self.tags.append(tag)

    def __enter__(self):
        self.level = len(self.tags) - 1
        if self.inline:
            print(f'{"  " * self.level}{self.open_tag}', end='')
        else:
            print(f'{"  " * self.level}{self.open_tag}')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.tags.pop()
        if self.inline:
            print(self.close_tag)
        else:
            print(f'{"  " * self.level}{self.close_tag}')

    def print(self, text):
        if self.inline:
            print(f"{text}", end='')
        else:
            print(f'  {"  " * self.level}{text}')


# TEST_1:
with HtmlTag('body') as _:
    with HtmlTag('h1') as header:
        header.print('Поколение Python')
    with HtmlTag('p') as section:
        section.print('Cерия курсов по языку программирования Python от команды BEEGEEK')

# TEST_2:
with HtmlTag('body') as _:
    with HtmlTag('h1', True) as header:
        header.print('Поколение Python')
    with HtmlTag('p', True) as section:
        section.print('Cерия курсов по языку программирования Python от команды BEEGEEK')

# TEST_3:
with HtmlTag('body') as _:
    with HtmlTag('h1', True) as header:
        header.print('Здесь есть что-то интересное')
    with HtmlTag('a', True) as section:
        section.print('https://stepik.org/media/attachments/course/98974/watch_me.mp4')

# TEST_4:
with HtmlTag('div') as _:
    with HtmlTag('p') as paragraph:
        with HtmlTag('strong', True) as strong:
            strong.print('Notice:')
        paragraph.print('Your browser is ancient')

# TEST_5:
with HtmlTag('table') as _:
    with HtmlTag('tr') as paragraph:
        with HtmlTag('th', True) as field:
            field.print('текст заголовка')
        with HtmlTag('td') as data:
            with HtmlTag('ul'):
                with HtmlTag('li', True) as marked_list:
                    marked_list.print('данные')
                with HtmlTag('li', True) as marked_list:
                    marked_list.print('данные')
                with HtmlTag('li', True) as marked_list:
                    marked_list.print('данные')
                with HtmlTag('li', True) as marked_list:
                    marked_list.print('данные')
                with HtmlTag('li', True) as marked_list:
                    marked_list.print('данные')
