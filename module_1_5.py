immutable_var=(1, True, 'srt')
print(immutable_var)
# immutable_var[0]=2 Картеж - это неизменяемый список, его элементы нельзя изменить. Только если в самом его списке не будет изменяемого элемента в квадратных скобках, например:
immutable_var_1=([1,'школа',3,'дом'], True, 'str')
immutable_var_1[0][2]=2 # первая квадратная скобка указывает на изменяемый элемент в картеже, а вторая указывает на порядковый номер уже в самом изменяемом списке.
print(immutable_var_1)
mutable_list= ['red','gray','blue','green','yellow','pink','black']
mutable_list[6]='white'
mutable_list.append('purple')
mutable_list.remove('yellow')
mutable_list.pop(0)
print(mutable_list)