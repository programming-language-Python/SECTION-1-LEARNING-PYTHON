class Person:

    def __init__(self, name):
        self.name = name
        self.__age = 20

    def print_info(self):
        print(f'Name: {self.name}, Age: {self.__age}')

    # Геттер
    # def get_age(self):
    #     return self.__age

    # Сеттер
    # def set_age(self, value):
    #     if value in range(1, 101):
    #         self.__age = value
    #     else:
    #         print('Wrong age')

    # обязательно с начало идёт геттер, а потом сеттер
    # превращается в метод геттер
    @property
    def age(self):
        return self.__age

    # превращается в метод сеттер
    @age.setter
    def age(self, value):
        if value in range(1, 101):
            self.__age = value
        else:
            print('Wrong age')
