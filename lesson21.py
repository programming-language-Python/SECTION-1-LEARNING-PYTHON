"""
Дан список words. Составьте из него список слов-палиндромов. Попробуйте это сделать двумя способами: произвольное решение и решение в одну строчку кода.
Дан список my_str со строками, часть из которых являются палиндромами. Составьте новый список строк-палиндромов.
"""

words = ['мадам', 'топот', 'test', 'madam', 'word']
my_str = ['Око за око', 'А роза упала на лапу Азора', 'Около Миши молоко']

# Способ 1
# palindromes = []
# for word in words:
#     if word == word[::-1]:
#         palindromes.append(word)

# Способ 2
palindromes = [word for word in words if word == word[::-1]]
print(palindromes)

palindrome_strings = []
for string in my_str:
    new_string = string.replace(' ', '').lower()
    if new_string == new_string[::-1]:
        palindrome_strings.append(string)
print(palindrome_strings)
