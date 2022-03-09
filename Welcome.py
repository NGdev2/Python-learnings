name = input('Как тебя зовут?:')
print('Hello', name)

"""num_1 = input('Введите первое число:')
num_2 = input('Введите второе число:')
res = int(num_1)+int(num_2)
print(res)

a = 100
if (a > 1):
    print('True\n')
elif (a == 0):
    print('null\n')
else:
    print('False')

print('All is okay!')
"""

"""i = 1000
sumost = 0
while (sumost<9) and (i>0):
    print(i)
    print('сумма остатка равна: ', sumost)
    #i = i / 2
    sumost = (sumost +i%3)
    i = i//3
"""

"""a = [a+b for a in 'list' if a !='l' for b in 'bear' if b !='r']
print(a)
"""

"""l = []
i = 3
while (len(l) < 4):
    l.append (i)
    i**=2
    print(l)
"""

"""i=34
while (i<=67):
    if (i%2 == 0):
        print(i, end=' ')
    i+=1
"""

'''l = [34, 'Skyrim', '419', 12]
print(l)
i=0
while (i<4):
    print(l[i])
    i+=1
print(l[1::-1]) #item[START:STOP:STEP]
'''

'''a = (13, 87, 'biqi', 43.12) #создан кортеж
b = [13, 87, 'biqi', 43.12] #создан список
print(a.__sizeof__())
print(b.__sizeof__())

c = tuple('Hello World!')
print(c)'''

'''a = {'name': 'Dmitry', 'name_2': 'Marat'}
print(a['name_2'])

b = dict (short='dict', long='dictionary')
print(b['short'], 'сокращенно от', b['long'])

c = dict.fromkeys(['a', 'b', 'c', 'd'], 1)
print(c)

d = {a: a**2 for a in range(7)}
print(d)
'''

'''person_ivan = {'name': {'first_name': 'Ivanov', 'last_name': 'Ivan', 'middle_name': 'Ivanovich'}, 'address': ['г. Ульяновск',
'ул. Совенок д.1, кв.6'], 'phone': {'home_phone': '239-39-39', 'mobile_phone': '8-919-220-115'}}
print(person_ivan.keys())
'''

'''a = set ('hello')
#b = {'321', 47} #2-ой способ задания множества. в отл. от словаря, отсутсвует ключ-значение, параметры задаются через запятую

a.add('a')
print(type(a))
print(a)

#b = {i**2 for i in range(15)}
b = frozenset ('hello')
print(type(b))
print(b)
'''

'''a = {70, 84.71, '45', '31', 45}
print(a)
x = 45
print(x in a) #выведет тру, если число х имеется в множестве
z = {37, 41, '55', 2.07}
print(a.isdisjoint(z)) #выведет тру, если отсутствуют повторяющиеся элементы
d = {70, 45}
print(type(d))
print(d == a)
'''

'''a = {70, '45', '31', 45}
b = {70, 84.71, '45', '31', 22, 'hey'}
#a.update(b) #объединение
#a.intersection_update(b) #одинаковые
#a.difference_update(b) #пересечение - элементы из множества a, отсутств. в b
a.symmetric_difference_update(b) # то-же что difference_update, только для элементов обоих множеств
print(a)
print(b)
c = {3, 2, 3 ,2, 1, 2, 3}
c.remove(3)
print(c)
c.discard(2) # то-же что и remove, но не выдает ошибку если в множестве отсутствует такой элемент
print(c)
'''
