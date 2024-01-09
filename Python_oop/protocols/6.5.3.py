class Closer:
    def __init__(self, obj):
        self.obj = obj

    def __enter__(self):
        return self.obj

    def __exit__(self, exc_type, exc_value, traceback):
        if hasattr(self.obj, 'close'):
            self.obj.close()
        else:
            print('Незакрываемый объект')


output = open('output.txt', 'w', encoding='utf-8')

with Closer(output) as file:
    print(file.closed)

print(file.closed)

with Closer(5) as i:
    i += 1

print(i)
