# try:
#     a, b = float(input('Введите делимое: ')), float(input('Введите делитель: '))
#     answer = a / b
#     print(f'Частное = {answer}')
# except ZeroDivisionError:
#     print('Делить на ноль нельзя!')
# except ValueError:
#     print('Введены некорректные данные')
# finally:
#     print('Расчеты завершены')


# Напишите программу, которая будет считывать числа из текстового файла и выводить их сумму.
# В файле каждое число расположено на новой строке.
# def sum_numbers_from_file(file_name):
#     sum = 0
#     try:
#         with open(file_name, 'r', encoding='utf-8') as file:
#             for line in file:
#                 number = int(line.strip())
#                 sum += number
#     except FileNotFoundError:
#         print('Файл не найден')
#     except ValueError:
#         print('Ошибка в файле - одна из строк не является числом')
#     return sum
#
# file_name = 'numders.txt'
# sum_numbers = sum_numbers_from_file(file_name)
# print(f'Сумма чисел из файла: {sum_numbers}')


# Напишите программу, которая будет запрашивать у пользователя путь к папке и имя файла, и выводить полный
# путь к этому файлу, если файл есть в заданной папке и всех её подпапках. В случае, если файл не найден,
# программа должна выводить сообщение "Файл не найден".

# import os
# def search_file(path, file_name):
#     for dir_path, dir_name, file_name in os.walk(path):
#         for file in file_name:
#             if file == file_name:
#                 return os.path.join(dir_path, file)
#     # return 'Файл не найден'
#
# path = input('Введите путь к папке: ')
# file_name = input('Введите имя файла: ')
# result = search_file(path, file_name)
# print(result)


# Напишите программу, которая будет считывать числа из заданного файла, суммировать их и выводить результат. Файл
# содержит числа, разделенные пробелами или новыми строками. Если в файле присутствуют не только числа,
# программа должна игнорировать их.

def sum_numbers_from_file(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            numbers = [int(line) for line in file.read().split() if line.isdigit()]
            return sum(numbers)
    except FileNotFoundError:
        return 'Файл не найден'

file_name = input('Введите имя файла: ')
result = sum_numbers_from_file(file_name)
print(result)