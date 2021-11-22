import random
# Задание 1
# Напишите функцию, которая принимает два числа и проверяет, делится ли первое
# на второе без остатка.

# def one():
#     a = int(input())
#     b = int(input())
#     if a % b == 0:
#         print('Да, {} делится на {} без остатка'.format(a, b))
#     else:
#         print('Нет, {} не делится на {} без остатка'.format(a, b))
#
#
# one()

# Задание 2
# Напишите функцию, которая принимает список и возвращает из него n
# случайных элементов.

# def two():
#     a = list((input('Введите чрез пробел элементы списка: ')).split())
#     n = int(input())
#     print(random.sample(a, n))
#
# two()

# Задание 3
# Напишите функцию, которая принимает строку и возвращает новую строку,
# составленную из n символов исходной строки.

# def two():
#     new_a = ''
#     a = input('Введите строку')
#     n = int(input())
#     random_index = random.sample(a, n)
#     for i in random_index:
#         new_a += i
#     print(new_a)
#
#
# two()

# Задание 4
# Напишите функцию, которая возвращает количество разрядов в целом числе.
# Например: 123 – 3; 009898 – 4.

# def zad_4():
#     num = abs(int(input('Введите число: ')))
#     i = 0
#     while num > 0:
#         num = num//10
#         i += 1
#     print('Кол-во разрядов числа - {}'.format(i))
#
# zad_4()

# Задание 5
# Напишите функцию, которая возвращает сумму цифр целого числа. Например:
# 123 – 6, 78 – 15.
# def five():
#     print(sum(map(int, list(input()))))
#
# five()

# Задание 6
# Напишите функцию, которая принимает набор операций для банковского счета и
# проверяет, можно ли провести такую транзакцию. Транзакция считается допустимой,
# если сумма на счету после ее выполнения не окажется отрицательной.
# Пример входных данных: [+340, -98, -65, +43, -180].

# def six():
#     operations = map(int, list(input().split()))
#     suum = 0
#     for i in operations:
#         suum += i
#     if suum >= 0:
#         print('Да, можно')
#     else:
#         print('Нет, нельзя')
#
# six()

# Задание 7
# Напишите функцию my_replace, которая принимает три аргумента (исходную
# строку; подстроку, которую нужно заменить; подстроку для замены) и выполняет
# замену всех вхождений подстроки на новую. Например:
# cabaccabadaba, aba, d – cdccddd

# def my_replace():
#     first_string = input()
#     in_string = input()
#     change_string = input()
#     result_string = first_string.split(in_string)
#     print(result_string)
#     empty_string = []
#     for i in result_string:
#         if i == '':
#             i = change_string
#             empty_string.append(i)
#         else:
#             empty_string.append(i)
#
#     print(''.join(empty_string))
#
# my_replace()

# Задание 8
# Вводится строка, включающая строчные и прописные буквы. Требуется вывести
# ту же строку в одном регистре, который зависит от того, каких букв больше. При
# равном количестве преобразовать в нижний регистр. Например, вводится строка
# "HeLLo World", она должна быть преобразована в "hello world", потому что в
# исходной строке малых букв больше.
# def eight():
#     line, upp, low = input(), 0, 0
#     for symb in line:
#         if symb.isalpha() and symb.isupper():
#             upp += 1
#         elif symb.isalpha() and symb.islower():
#             low += 1
#     if upp > low:
#         print(line.upper())
#     else:
#         print(line.lower())
#
# eight()

# Задание 9
# Дана строка, в которой буква h встречается минимум два раза. Удалите из этой
# строки первое и последнее вхождение буквы h, а также все символы, находящиеся
# между ними.

# def nine():
#     s = input()
#     s = s[:s.find('h')] + s[s.rfind('h') + 1:]
#     print(s)
#
# nine()