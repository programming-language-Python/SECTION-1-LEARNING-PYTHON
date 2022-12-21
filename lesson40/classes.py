# родительский класс. Его ещё также называют базовый класс (base class), parent class, super class
class Person:

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def print_info(self):
        print(f'Name: {self.name}, Age: {self.__age}')

    # def get_age(self):
    #     return self.__age
    #
    # def set_age(self, value):
    #     if value in range(1, 101):
    #         self.__age = value
    #     else:
    #         print('Wrong age')

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value in range(1, 101):
            self.__age = value
        else:
            print('Wrong age')


# Класс наследник. Его ещё также называют дочерний класс, под класс (sub class)
# наследует все публичные методы и свойства
class Employee(Person):
    company = 'Google'

    def more_info(self):
        print(f'{self.name} works in {self.company}')
