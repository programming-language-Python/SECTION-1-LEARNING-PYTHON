def get_sum(a, b):
    """
    Возращает сумму аргументов a и b.

    :param a: Первый операнд
    :type a: int
    :param b: Второй операнд
    :type b: int
    :return: Return type int
    """
    return a + b


# print(get_sum(1, 2))

# a = 5 # global. В функциях доступна только для чтения

# def f():
#     a = 10 # local
#     a += 1
#     print(a)
#
# print(a)
# f()
# print(a)

# def f():
#     global a
#     a += 1
#     print(a)
#
# print(a)
# f()
# print(a)


l = [1, '2', 3]


def f(l):
    return [i * 2 for i in l]


print(f(l))


def f2(l):
    def get_mult(x):
        return int(x) * 2

    return [get_mult(i) for i in l]


print(f2(l))


def f3(l):
    def get_mult(x):
        if isinstance(x, int):
            return x * 2

    return [get_mult(i) for i in l if get_mult(i)]


print(f3(l))


def f4(l):
    def get_mult(x):
        return x * 2

    return list(map(get_mult, l))


print(f4(l))

"""
1. Дан массив, в котором среди прочих элементов есть слово "odd" (нечетный). Определите, есть ли в списке число, которое является индексом элемента "odd". Напишите функцию, которая будет возвращать True или False, соответсвенно.
"""


def odd_ball(arr):
    """
    Проверяет есть ли в списке цифра совпадающая с позицией строки "odd".

    :param arr:
    :type arr: list
    :return: bool
    """
    return arr.index("odd") in arr


print(odd_ball(["even", 4, "even", 7, "even", 55, "even", 6, "even", 10, "odd", 3, "even"]))  # True
print(odd_ball(["even", 4, "even", 7, "even", 55, "even", 6, "even", 9, "odd", 3, "even"]))  # False
print(odd_ball(["even", 10, "odd", 2, "even"]))  # True

"""
2. Напишите функцию find_sum(n), где аргумент функции - это конечный элемент последовательности включительно. Функция должна вернуть сумму всех чисел последовательности, кратных 3 или 5. Попробуйте решить задачу двумя способами (один из способов в одну строчку кода).
"""


def find_sum(n):
    """
    Возращает сумму чисел кратным 3 или 5.

    :param n: конечное число
    :type n: int
    :return: сумма
    """
    # Способ № 1
    # n += 1
    # amount = 0
    # for i in range(1, n):
    #     if i % 3 == 0 or i % 5 == 0:
    #         amount += i
    # return amount

    # Способ № 2
    return sum([i for i in range(1, n + 1) if i % 3 == 0 or i % 5 == 0])


print(find_sum(5))  # return 8 (3 + 5)
print(find_sum(10))  # return 33 (3 + 5 + 6 + 9 + 10)

"""
3. Дан список имен. Выберите в новый список только те имена, которые состоят из 4-х букв.
names = ["Ryan", "Kieran", "Mark", "John", "David", "Paul"] # ["Ryan", "Mark", "John", "Paul"]
"""

names = ["Ryan", "Kieran", "Mark", "John", "David", "Paul"]


def get_names(names):
    """
    Возращает список имён с 4 буквами

    :param names: имена
    :type names: list
    :return: Return type list
    """
    return [name for name in names if len(name) == 4]


print(get_names(names))
