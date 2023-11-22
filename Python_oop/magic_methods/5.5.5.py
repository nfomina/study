class Queue:
    def __init__(self, *args):
        self.queue = []
        for arg in args:
            self.queue.append(arg)

    def __str__(self):
        return f'{" -> ".join(map(str, self.queue))}'

    def add(self, *args):
        self.queue.extend(args)

    def pop(self):
        if self.queue:
            first = self.queue[0]
            self.queue = self.queue[1:]
            return first
        else:
            return None

    def __eq__(self, other):
        return self.queue == other.queue

    def __add__(self, other):
        if isinstance(other, Queue):
            return Queue(*self.queue + other.queue)
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Queue):
            self.queue += other.queue
            return self
        return NotImplemented

    def __rshift__(self, n):
        if isinstance(n, int):
            if n >= len(self.queue):
                return Queue()
            else:
                return Queue(*self.queue[n:])
        return NotImplemented


queue = Queue(1, 2)
queue.add(3)
queue.add(4, 5)

print(queue)
print(queue.pop())
print(queue)

queue1 = Queue(1, 2, 3)
queue2 = Queue(1, 2)

print(queue1 == queue2)
queue2.add(3)
print(queue1 == queue2)

queue1 = Queue(1, 2, 3)
queue2 = Queue(4, 5)

print(queue1 + queue2)

queue1 = Queue(1, 2, 3)
queue2 = Queue(4, 5)

queue1 += queue2

print(queue1)

queue = Queue(1, 2, 3, 4, 5)

print(queue >> 3)

# TEST_6:
queue = Queue(1, 2, 3, 4, 5)
id1 = id(queue)
print(queue)

queue += Queue(6, 7, 8, 9, 10)
id2 = id(queue)

print(queue)
print(id1 == id2)

queue = queue + Queue(11, 12, 13, 14, 15)
id3 = id(queue)

print(queue)
print(id1 == id3)

# TEST_7:
print('TEST_7')
queue = Queue(*'beegeek')
for i in range(9):
    print(f'Queue >> {i} =', queue >> i)

# TEST_8:
queue = Queue(1)
item = queue.pop()
print(item)
print(queue.pop())

# TEST_9:
q1 = Queue(1, 2)
q2 = Queue(1, 2)

print(q1 == q2)
print(q1 != q2)

# TEST_10:
queue = Queue(1, 2, 3)
print(queue.__add__([]))
print(queue.__iadd__('bee'))
print(queue.__rshift__('geek'))
