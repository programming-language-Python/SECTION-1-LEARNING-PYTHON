"""
1. Дан список. Получите новый список, в котором каждое значение будет удвоено:
[1, 2, 3] --> [2, 4, 6]
"""

l1 = [1, 2, 3]
l2 = [i * 2 for i in l1]
print('Ответ на задание 1:', l2)

"""
2. Дан список. Возведите в квадрат каждый из его элементов и получит сумму всех полученных квадратов:
[1, 2, 3] --> 14 --> 1^2 + 2^2 + 3^2 = 14
"""

amount = 0
for i in l1:
    amount += i ** 2
print('Ответ на задание 2:', amount)

"""
3. Игорь любит кататься на велосипеде. Он знает, что при этом важно не допустить обезвоживания и пьет 0,5 литра воды в час. Вам дается время в часах, и вам нужно вернуть количество литров, которые Игорь выпьет, с округлением до наименьшего значения.
time1 = 3 --> litres = 1
time2 = 6.7 --> litres = 3
time3 = 11.8 --> litres = 5
"""

time1 = 3
time2 = 6.7
time3 = 11.8
lister1 = int(time1 * .5)
lister2 = time2 * .5 // 1
lister3 = int(time3 * .5)
print(f'Ответ на задание 3: {lister1}, {lister2}, {lister3}')

"""
4. Дана строка 'Hello world'. Проверьте, если в этой строке есть символ пробела - " ", тогда преобразуйте строку к верхнему регистру, если же нет, тогда к нижнему.
***************
s = 'Hello world'
if stm:
	pass
else:
	pass
"""

s = 'Hello world'
stm = ' ' in s
if stm:
    s = s.upper()
else:
    s = s.lower()
print('Ответ на задание 4:', s)
