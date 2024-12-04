calls = 0
def  count_calls() :
    global calls
    calls += 1
def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())
def is_contains (string, list_to_search):
    count_calls()
    return string.lower() in [i.lower() for i in list_to_search]


print(string_info('SketchBook'))
print(string_info('FOG'))

print(is_contains('aPPle', ['avocAdo', 'APPLE', 'lime', 'mango', 'pineaPPle']))
print(is_contains('aPPle', ['avocAdo', 'lime', 'mango', 'pineaPPle']))
print(is_contains('granite', ['asphalt', 'concrete', 'limestone']))

print(calls)