int_list = []
n = int(input())
for i in range(n):
    int_list += [int(input())]
print(int_list)


def count(variable):
    counter = 0
    for i in int_list:
        if i < variable:
            counter += 1
    return counter


def output(func):
    def wrap():
        m = func()
        print('количество запросов', m)
        return m

    def res():
        for i in range(wrap()):
            int_queries = int(input())
            summ = count(int_queries)
            print(summ)

    return res()


@output
def queries():
    return int(input('Введите количество запросов: '))

queries