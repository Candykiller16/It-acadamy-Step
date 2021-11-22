# Задание 1
# Напишите функцию, которая читает данные из файла и записывает в новый файл:
# • количество чисел во входном файле;
# • самое большое число во входном файле;
# • самое маленькое число во входном файле;
# • среднее арифметическое всех чисел во входном файле;
# • количество четных чисел во входном файле.
# Входные файлы: files_input1.txt, files_input2.txt.
#

# def task_1(file):
#     with open(file, 'r') as foul:
#         list_for_1 = []
#         for i in foul:
#             list_for_1.append(int(i.replace('\n', '')))
#         even_numbers = 0
#         for j in list_for_1:
#             if j % 2 == 0:
#                 even_numbers += 1
#     kol, maximum, minimum, average = len(list_for_1), max(list_for_1), min(list_for_1), sum(list_for_1) / len(
#         list_for_1)
#     with open('for_first_task.txt', 'w') as w:
#         w.write('Колличество чисел = {}\n'.format(kol))
#         w.write('Самое большое число во входном файле = {}\n'.format(maximum))
#         w.write('Среднее арифметическое всех чисел во входном файле = {}\n'.format(average))
#         w.write('Количество четных чисел во входном файле = {}\n'.format(even_numbers))
#
# task_1('files_input1.txt')
# task_1('files_input2.txt')

# Задание 2
# Напишите функцию, которая читает данные из файла и выводит в отдельный
# файл:
# • количество чисел во входном файле;
# • самое большое число во входном файле;
# • самое маленькое число во входном файле.
# Входной файл: files_input3.txt.


# def task_2(file):
#     list_2 = []
#     with open(file, 'r') as f:
#         for line in f:
#             try:
#                 list_2.append(int(line.strip()))
#             except ValueError:
#                 continue
#
#     kol = len(list_2)
#     maximum = max(list_2)
#     minimum = min(list_2)
#     with open('for_second_task.txt', 'w') as w:
#         w.write('количество чисел во входном файле = {}\n'.format(kol))
#         w.write('Самое большое число во входном файле = {}\n'.format(maximum))
#         w.write('Самое маленькое число во входном файле = {}\n'.format(minimum))
#
# task_2('files_input3.txt')


# Задание 3
# Напишите функцию, которая читает данные из файла и выводит в отдельные
# файлы:
# • числа;
# • строки.
# Входной файл: files_input3.txt.


# def task_3(file):
#     first_list = []
#     with open(file, 'r') as f:
#         for line in f:
#             first_list.append(line.replace('\n', ''))
#     list_for_str = []
#     list_for_int = []
#     for i in first_list:
#         try:
#             list_for_int.append(int(i))
#         except ValueError:
#             list_for_str.append(i)
#     with open('for_third_task_str', 'w') as f_str:
#         for st in list_for_str:
#             f_str.write(st + '\n')
#     with open('for_third_task_int', 'w') as f_int:
#         for num in list_for_int:
#             f_int.write(str(num) + '\n')
#
# task_3('files_input3.txt')

# Задание 4
# Напишите функцию, которая читает данные из файла и выводит в отдельный
# файл:
# • тот же текст в верхнем регистре;
# • тот же текст в нижнем регистре.
# Входные файлы: files_input4.txt, files_input5.txt.

# def task_4(file):
#     tekst = ''
#     with open(file, 'r') as f:
#         for i in f:
#             tekst += i
#     with open('for_fourth_task_up.txt', 'w') as up:
#         up.write(tekst.upper())
#     with open('for_fourth_task_low.txt', 'w') as low:
#         low.write(tekst.lower())
#
#
# task_4('files_input4.txt')
# task_4('files_input5.txt')

# Задание 5
# Напишите функцию, которая читает данные из файла и выводит в отдельный
# файл:
# • количество слов в файле;
# • среднюю длину слова (без учета пунктуации).
# Входные файлы: files_input4.txt, files_input5.txt.


# def task_5(file):
#     tekst = []
#     with open(file, 'r') as f:
#         for line in f:
#             for lines in line.split():
#                 for split0 in lines.split(' '):
#                     for split1 in split0.split(','):
#                         for split2 in split1.split('.'):
#                             for split3 in split2.split('?'):
#                                 for split4 in split3.split('!'):
#                                     for word in split4.split(':'):
#                                         if word != "":
#                                             tekst.append(word)
#         list_for_letter = []
#         for i in tekst:
#             for j in i:
#                 list_for_letter.append(j)
#         a = len(list_for_letter)
#     length = len(tekst)
#     with open('for_fiwth_task.txt', 'w') as w:
#         w.write('Количество слов в файле = {}\n'.format(length))
#         w.write('Среднюю длина слова (без учета пунктуации) = {}\n'.format(a / length))
#
#
# task_5('files_input4.txt')
# task_5('files_input5.txt')
