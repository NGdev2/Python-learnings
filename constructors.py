# class Person(object):
#     def __init__(self, name):
#         self.name = name
#
#
# class Student(Person):
#     def __init__(self, something):
#         if isinstance(something, Person):
#             self.__dict__ = something.__dict__.copy()
#         elif isinstance(something, str):
#             super(Student, self).__init__(something)
#         else:
#             raise Exception('Wrong arguments!')
#
#
# airat = Person('Airat')
# print(airat.name)
#
# bulat = Student('Bulat')
# print(bulat.name)
#
# marat = Student(airat)
# print(marat.name)


# конструктор это когда при создание объекта сразу задаем характеристики

class Person:
    name = ''
    age = '12'

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student (Person):
    course = 1

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course


igor = Student('Игорь', 17, 4)
print(igor.name, igor.age, 'лет,', igor.course, end='-ый курс\n')

vasya = Student('Василий', '18', 3)
print(vasya.name, vasya.age, 'лет,', vasya.course, '-ый курс')
# print(vasya.__dir__())
