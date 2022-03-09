'''def func(x, a):
    res = x + a
    return res
print (func('Hey, ', 'there!'))
'''
'''def func (x):
    def add(a):
        return a + x
    return add
test = func(1)
print(test(2))
'''
'''def square(length):
    def operate(weight):
        res = length * weight
        return res
    return operate
floor = square(37)
call = floor(21)
print(call)
'''
'''def func (i, j, Pi = 3.14): #параметр по умолчанию, который при вызову может быть изменен
    return (i+j)*Pi

print(func(1,2))'''
'''def func(*args): #задать функцию, не знаю о количестве параметров. *-кортеж, **-словарь
    return args
z = func('sd', 17, 313.21)
print(z)
print(type(z))

def func(**args): #задать функцию, не знаю о количестве параметров. *-кортеж, **-словарь
    return args
z = func(a=17,b=23,c=47,d='eqs')
print(z)
print(type(z))
'''
'''
add = lambda x, y: x / y #подвид функции, ноупрощенный - 1-строчный
print(add(7, 3))
#упрощенный вид:
print((lambda x, y: x**y)(3, 5))'''

'''x = int (input())
y = int (input())

try:
    res = x / y
except ZeroDivisionError:
    print('Вы ввели нуль')
    res = 0
print(res)'''

try:
    x = int(input('введите число '))
except ValueError:
    print('Вы ввели не число')
    x = 0
else:
    print('Все Ок')

try:
    y = int(input('введите число '))
except ValueError:
    print('Вы ввели не число')
    y = 0
else:
    print('Все Ок')
finally:
    print('finally выполняется всегда, независимо от наличия или отсутствия ошибки')

try:
    res = x / y
except ZeroDivisionError:
    print('Вы ввели нуль')
    res = 0
print(res)