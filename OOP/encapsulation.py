# class Person:
#     name =''
#     age = '12'
#     surname = ''
#     __nation = 'russian'
#
#     def set (self, name, surname, age, __nation):
#         self.name = name
#         self.surname = surname
#         self.age = age
#         self.__nation = __nation
# dima = Person()
# dima.set('Dmitriy', 'Venkov', '17', 'rus')
# print(dima.__dict__)

class Person:
    name =''
    age = '12'

    def __set (self, name, age):
        self.name = name
        self.age = age

class Student (Person):
    course = 1

igor = Student()
igor._Person__set ('Igor', '17') # обратиться к подобной инкапсуляции можно через класс с одним подчеркиванием
print(igor.name, igor.age, igor.course)
#полиморфизм это метод который выполняется по разному для разных классов(пример: 2+2 = 4; "2"+"2" = "22"