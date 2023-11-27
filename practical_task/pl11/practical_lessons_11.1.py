# Написание программы, запрашиваеющей у пользователя название файла для записи и строку, которая будет записана
# в заданный текстовый файл.  Случай, когда заданного имени файла не существует и вывод сообщения об этом на экран.
# try:
#     f = input('Введите имя файла: ')
#     s = input('Введите строку текста для вставки: ')
#     file = open(f, 'r+', encoding='utf-8')
#     file.write(s)
#     print(f'Текст записан в файл {f}')
#     file.close()
# except FileNotFoundError:
#     print(f'Файл {f} не найден')
# finally:
#     print('Работа программы завершена')


# Напишите программу, которая считывает строку текста и записывает её в текстовый файл output.txt.
# with open('output.txt', 'w', encoding='utf-8') as file:
#     file.write(input('Введите текст: '))


# Напишите программу, записывающую в текстовый файл random.txt 40 случайных чисел в диапазоне
# от 111 до 888 (включительно), каждое с новой строки.

# with open('random.txt', 'w', encoding='utf-8') as output:
#     import random
#     for _ in range(40):
#         print(random.randint(111, 888), file=output)


# Вам доступен текстовый файл input.txt, состоящий из нескольких строк. Напишите программу для записи
# содержимого этого файла в файл output.txt в виде нумерованного списка, где перед каждой строкой стоит ее номер,
# символ ) и пробел. Нумерация строк должна начинаться с 1.
# with open('input.txt', 'r', encoding='utf-8') as file_input:
#     line = file_input.readlines()
#
# with open('output.txt', 'w', encoding='utf-8') as file_output:
#     for count, item in enumerate(line, 1):
#         print(str(count) + ')', item, file=file_output, end='')


# Вам доступен текстовый файл class_scores.txt с оценками за итоговый тест на строках вида:
# фамилия оценка (фамилия и оценка разделены пробелом). Оценка - целое число от 0 до 100 включительно.
# Напишите программу для добавления 5 баллов к каждому результату теста и вывода фамилий и
# новых результатов тестов в файл new_scores.txt.
# with open('class_scores.txt', 'r', encoding='utf-8') as file_input:
#     line_list = file_input.readlines()
#     file_input.seek(0)
#     line = file_input.readline().rstrip().split()
#     with open('new_scores.txt', 'w', encoding='utf-8') as file_output:
#         new_score = 0
#         for _ in range(len(line_list)):
#             new_score = int(line[1]) + 5
#             if new_score > 100:
#                 new_score = 100
#             line[1] = str(new_score)
#             print(*line, file=file_output)
#             line = file_input.readline().rstrip().split()


# Напишите программу, которая открывает файл "numbers.txt" и суммирует все числа, записанные в этом файле.
# Если во время чтения файла возникает ошибка, программа должна вывести сообщение
# "Ошибка чтения файла" и завершиться с кодом ошибки 1.

# try:
#     with open('numbers.txt', 'r', encoding='utf-8') as file:
#         numbers = file.readlines()
#         result = 0
#         for number in numbers:
#             result += int(number.strip())
#         print(f'Сумма чисел равна {result}')
# except IOError:
#     print('Ошибка чтения файла')
#     exit(1)


# Напишите программу, которая открывает файл "data.txt" и записывает в него новую строку с текущей датой и временем.
# Если во время записи файла возникает ошибка, программа должна вывести сообщение "Ошибка записи файла"
# и завершиться с кодом ошибки 1.

# from datetime import datetime
#
# try:
#     file = open('data.txt', 'a', encoding='utf-8')
#     now = datetime.now()
#     data_time = now.strftime("%d/%m/%Y %H:%M:%S")
#     file.write(data_time + '\n')
#     file.close()
# except IOError:
#     print('Ошибка записи файла')
#     exit(1)


# Напишите программу, которая открывает файл "text.txt" и выводит его содержимое на экран. Если файл не существует,
# программа должна вывести сообщение "Файл не найден" и завершиться с кодом ошибки 1.
# try:
#     file = open('D:/pythonProject/practical_task/pl10/text.txt', 'r', encoding='utf-8')
#     content = file.read()
#     file.close()
#     print(content)
# except IOError:
#     print('Файл не найден')
#     exit(1)


# Напишите программу, которая открывает файл "students.csv" и считывает информацию о студентах.
# Файл содержит данные в формате CSV: каждая строка представляет собой запись одного студента,
# а значения разделены запятой. Программа должна подсчитать количество записей и вывести его на экран.
# Если файл не существует или возникает ошибка чтения файла, программа должна вывести сообщение
# "Ошибка чтения файла" и завершиться с кодом ошибки 1.

# import csv
#
# try:
#     with open('students.csv', 'r', encoding='utf-8') as file:
#         students = list(csv.reader(file))
#         count = len(students)
#         print(f'Количество студентов: {count}')
# except IOError:
#     print('Ошибка чтения файла')
#     exit(1)