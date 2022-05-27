

def key_difference(dict1, dict2):
    result = {}
    for key in dict1.keys():
        if dict2.get(key):
            if dict1[key] == dict2[key]:
               result[key] = 'equal'
            else:
                result[key] = 'changed'
        else:
            result[key] = 'deleted'
    for key in dict2.keys():
        if key not in dict1.keys():
            result[key] = 'added'
    return result





dict1 = {'one': 'eon', 'two': 'two', 'four': 'True'}
dict2 = {}

result = key_difference(dict1, dict2)

print(result)
# Sample Output 2:
#
# {'one': 'deleted', 'two': 'deleted', 'four': 'deleted'}