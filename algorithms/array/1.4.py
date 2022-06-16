
queue = []

while True:
    line = input()
    if line:
        if line == '+':
            if queue:
                print(queue[0])
                queue = queue[1:]
        elif len(queue) < 5:
            queue.append(line)
    else:
        break
