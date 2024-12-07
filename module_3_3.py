print('1.Функция с параметрами по умолчанию: ')

def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params('str', True, 1)
print_params( c = 1, a = 'str', b = 1)
print_params('str', c = 'str')

print_params(b = 25)
print_params(c = [1,2,3])

print('2.Распаковка параметров: ')

values_list = (1, 'int', False)
values_dict = {'a': 'str', 'b': 2, 'c': True}
def print_params(a, b , c):
    print(a, b , c)
print_params(*values_list)
print_params(**values_dict)
print_params(values_list, values_dict, 3)

print('3.Распаковка + отдельные параметры: ')

values_list_2 = [ 777, 'Lusk']
print_params(*values_list_2, 42)
