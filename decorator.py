def decorator(func):
    def wrapper(): # обертка декоратора
        print('До выполнения функции')
        func()
        print('После выполнения функции')
    return wrapper

@decorator # либо показать декоратор таким образом
def show():
    print('для декоратора')
show = decorator (show)
#           либо добавить переменную с вызовом декоратора
show()
decorator (show)

