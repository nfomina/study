class AttrsNumberObject:
    def __init__(self, **kwargs):
        self.attrs_num = 1
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __setattr__(self, name, value):
        object.__setattr__(self, name, value)

    def __getattribute__(self, item):
        if item == 'attrs_num':
            return len(self.__dict__)
        return object.__getattribute__(self, item)


music_group = AttrsNumberObject(name='Silent Poets', genre='acid jazz')

print(music_group.attrs_num)

music_group = AttrsNumberObject()

print(music_group.attrs_num)

music_group = AttrsNumberObject(name='Woodkid', genre='pop')

print(music_group.attrs_num)
music_group.country = 'France'
print(music_group.attrs_num)

music_group = AttrsNumberObject(name='Alexandra Savior', genre='dream pop')

print(music_group.attrs_num)
del music_group.genre
print(music_group.attrs_num)