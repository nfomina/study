from time import perf_counter


class AdvancedTimer:
    def __init__(self):
        self.last_run = None
        self.runs = []
        self.min = None
        self.max = None

    def __enter__(self):
        self.start = perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = perf_counter() - self.start
        self.last_run = self.end
        self.runs.append(self.end)
        self.min = min(self.runs)
        self.max = max(self.runs)


# TEST_1:
timer = AdvancedTimer()

print(timer.runs)
print(timer.last_run)
print(timer.min)
print(timer.max)

# TEST_2:
from time import sleep

timer = AdvancedTimer()

with timer:
    sleep(1.5)
print(round(timer.last_run, 1))

with timer:
    sleep(0.7)
print(round(timer.last_run, 1))

with timer:
    sleep(1)
print(round(timer.last_run, 1))

# TEST_3:
from time import sleep

timer = AdvancedTimer()

with timer:
    sleep(1.5)

with timer:
    sleep(0.7)

with timer:
    sleep(1)

print([round(runtime, 1) for runtime in timer.runs])
print(round(timer.min, 1))
print(round(timer.max, 1))

# TEST_4:
import time


def func1():
    time.sleep(1.3)
    return


def func2():
    time.sleep(1.7)
    return


def func3():
    time.sleep(1.1)
    return


def func4():
    time.sleep(0.3)
    return


timer = AdvancedTimer()

funcs = [func2, func1, func4, func3]

for func in funcs:
    with timer:
        func()

print([round(runtime, 1) for runtime in timer.runs])
print(round(timer.last_run, 1))
print(round(timer.min, 1))
print(round(timer.max, 1))
