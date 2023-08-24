class Todo:
    def __init__(self):
        self.things = []
        self.min = None
        self.max = None

    def add(self, task, priority):
        if self.min and self.max:
            if priority < self.min:
                self.min = priority
            if priority > self.max:
                self.max = priority
        else:
            self.min = self.max = priority
        self.things.append((task, priority))

    def get_by_priority(self, n):
        return [item[0] for item in filter(lambda a: a[1] == n, self.things)]

    def get_low_priority(self):
        return self.get_by_priority(self.min)

    def get_high_priority(self):
        return self.get_by_priority(self.max)


todo = Todo()

print(todo.things)
print(todo.get_by_priority(1))
print(todo.get_low_priority())
print(todo.get_high_priority())

todo = Todo()

todo.add('Проснуться', 3)
todo.add('Помыться', 2)
todo.add('Поесть', 2)

print(todo.get_by_priority(2))

todo = Todo()

todo.add('Ответить на вопросы', 5)
todo.add('Сделать картинки', 1)
todo.add('Доделать задачи', 4)
todo.add('Дописать конспект', 5)

print(todo.get_low_priority())
print(todo.get_high_priority())
print(todo.get_by_priority(3))
