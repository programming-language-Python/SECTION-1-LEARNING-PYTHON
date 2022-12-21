# https://docs.python.org/3/library/

# import os
# import random as r  # псевдоним
# import random
# from random import randint, shuffle
# from random import *

# print(os.getcwd())
# # print(random.randint(1, 100))
#
# print(randint(1, 100))
# l = [1, 2, 3, 4, 5]
# shuffle(l)
# print(l)


import libs

from lesson24 import input_number

print(__name__)
# print(libs.get_count('hello', 'l'))
# print(libs.get_len('hello'))

f = libs.get_count
print(f('hello', 'l'))


def get_sum(a, b):
    return a + b


func = get_sum
print(func(1, 2))

'''
Создайте игру "Угадай число". В коде программы в переменную запишите любое число от 1 до 100 (в следующих уроках мы узнаем, как генерировать случайное число), которое и должен угадать игрок. Далее программа должна спросить у игрока угадать число. Если пользователь не угадал число - программа сообщает, что загаданное число больше/меньше и предлагает попробовать еще раз, при этом программа ведет счета кол-ва попыток игрока. Если игрок угадал число, тогда программа благодарит за игру и сообщает кол-во попыток, за которое было угадано число.
Сделать чтоб игра генерировало число рандомно и спрашивала у пользователя "Продолжить игру?"
'''
from random import randint


def continue_game():
    global number_of_attempts
    random_number = randint(1, 100)
    input_number = 0
    number_of_attempts = 0
    while input_number != random_number:
        input_number = int(input('Какое число я загадал от 1 до 100? '))
        number_of_attempts += 1
        if random_number > input_number:
            print('Загаданное число больше')
        elif random_number < input_number:
            print('Загаданное число меньше')
    return f'Благодарю за игру и ваше кол-во попыток за которое угадали число: {number_of_attempts}'


while True:
    is_continue_game = input('Хотите продолжить игру? ')
    if is_continue_game == 'да':
        print(continue_game())
    elif is_continue_game == 'нет':
        break
    else:
        print('Такой ответ не принимается')
