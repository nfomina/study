def sourcetemplate(url):
    def add_param(**params):
        return url + '?' + '&'.join(["{}={}".format(k, v) for k, v in sorted(params.items())]) if params else url
    return add_param


url = 'https://beegeek.ru'
load = sourcetemplate(url)
print(load(name='timur'))
# https://beegeek.ru?name=timur

url = 'https://stepik.org/lesson/651459/step/14'
load = sourcetemplate(url)
print(load(thread='solutions', unit=648165))
# https://stepik.org/lesson/651459/step/14?thread=solutions&unit=648165

url = 'https://beegeek.ru'
load = sourcetemplate(url)
print(load())
# https://beegeek.ru

# TEST_4:
url = 'https://all_for_comfort_life.com'
load = sourcetemplate(url)
print(load(smartphone='iPhone', notebook='huawei', sale=True))
# https://all_for_comfort_life.com?notebook=huawei&sale=True&smartphone=iPhone

# TEST_5:
url = 'https://hide_and_seek.harvard'
load = sourcetemplate(url)
print(load(wizard='Dambldor', magic_wand='elderberry', thief='Volandemord'))
# https://hide_and_seek.harvard?magic_wand=elderberry&thief=Volandemord&wizard=Dambldor
