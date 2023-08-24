from inflection import camelize, underscore


class CaseHelper:
    def __init__(self):
        pass

    @staticmethod
    def is_snake(string):
        if underscore(string) == string and '__' not in string:
            return True
        return False

    @staticmethod
    def is_upper_camel(string):
        if camelize(string) == string:
            return True
        return False

    @staticmethod
    def to_snake(string):
        return underscore(string)

    @staticmethod
    def to_upper_camel(string):
        return camelize(string)


print(CaseHelper.is_snake('beegeek'))
print(CaseHelper.is_snake('bee_geek'))
print(CaseHelper.is_snake('Beegeek'))
print(CaseHelper.is_snake('BeeGeek'))
# True
# True
# False
# False
print(CaseHelper.is_upper_camel('beegeek'))
print(CaseHelper.is_upper_camel('bee_geek'))
print(CaseHelper.is_upper_camel('Beegeek'))
print(CaseHelper.is_upper_camel('BeeGeek'))
# False
# False
# True
# True
print(CaseHelper.to_snake('Beegeek'))
print(CaseHelper.to_snake('BeeGeek'))
# beegeek
# bee_geek
print(CaseHelper.to_upper_camel('beegeek'))
print(CaseHelper.to_upper_camel('bee_geek'))
# Beegeek
# BeeGeek
cases = ['assert_equal', 'tear_down', '__init__', 'assertEqual', 'setUp', 'tearDown', 'run', 'exit', 'setup']

for case in cases:
    print(CaseHelper.is_snake(case))

# TEST_6:
cases = ['assert_equal', 'tear_down', '__init__', 'assertEqual', 'setUp', 'tearDown', 'run', 'exit', 'setup', 'AssertEqual', 'SetUp']

for case in cases:
    print(CaseHelper.is_upper_camel(case))

# TEST_7:
cases = ['AssertEqual', 'SetUp', 'TearDown', 'AddModuleCleanup', 'AssertRaisesRegex', 'AssertAlmostEqual', 'AssertNotAlmostEqual']

for case in cases:
    print(CaseHelper.to_snake(case))

# TEST_8:
cases = ['assert_equal', 'tear_down', 'assert_raises_regex', 'assert_almost_equal', 'assert_not_almost_equal', 'beegeek']

for case in cases:
    print(CaseHelper.to_upper_camel(case))
