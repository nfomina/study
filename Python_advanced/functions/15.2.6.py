def info_kwargs(**kwargs):
    for item in sorted(kwargs):
        print(f'{item}: {kwargs[item]}')


info_kwargs(first_name='Timur', last_name='Guev', age=28, job='teacher')
# age: 28
# first_name: Timur
# job: teacher
# last_name: Guev