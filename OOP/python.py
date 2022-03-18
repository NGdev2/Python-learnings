class Person:
    name = 'Person_name'
    age = '16'
    # в классах функции называются методами а переменные называются полями
    def set(self, name, age): #в python есть условная инкапсуляция, которая не запрещает доступ к методам класса и никак не влияет,
        # но советует программистам не менять значения класса задать её можно нижним подчеркиванием: _ Например:
        # _gender = 'male'
        # Имеется более строгая защита __ Но и она подвержена изменениям
        self.name = name
        self.age = age
# в каждом методе должен быть аргумент 'self'.
# Это обязательный аргумент, содержащий в себе экземпляр класса, передающийся при вызове метода

class Student (Person): #Наследование от класса Person
    course = 1

vlad = Person()
vlad.age = '21'
vlad.name = 'Владислав'
print(vlad.name, vlad.age)

maks = Person()
maks.set ('Максим', '27')
print(maks.name + ', ' + str(maks.age) + ' лет')

marat = Student()
marat.set('Марат', '20')
marat.course = 2
