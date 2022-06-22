

start_queue = 0
queue = 0
for item in [int(i) for i in input().split()]:
    if item == 0:
        queue+=1
    else:
        if queue == 0:
            start_queue += 1
        else:
            queue -= 1
print(start_queue)