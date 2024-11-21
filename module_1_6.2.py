my_dict={'Anna' :1997, 'Ivan':1995, 'Max': 1990 }
print(my_dict)
print(my_dict['Anna'])
print(my_dict.get('Anastasiya'))
my_dict.update({'Alex': 1955,
                'Ludmila': 1965})
c= my_dict.pop('Ivan')
print(c)
print(my_dict)
my_set={'Book', 1 , True, 3, 'Apple', 1, 2, 3, 'Apple', True}
print(my_set)
my_sett=(5, 6)
my_set.update(my_sett)
my_set.discard('Apple')
print(my_set)