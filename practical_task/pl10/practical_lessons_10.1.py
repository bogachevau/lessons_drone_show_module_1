# На вход программе подается строка с именем текстового файла. Напишите программу,
# которая выводит на экран его содержимое.
#
# file = open(input(), 'r', encoding='utf-8')
# line = file.read()
# print(line)
# file.close()

# На вход программе подается строка с именем текстового файла. Напишите программу, которая выводит
# на экран его предпоследнюю строку.

# with open(input(), encoding='utf-8') as file:
#     line = file.readlines()
#     print(line[-2])


with open('file.txt', encoding='utf-8') as file:
    lines = file.readlines()
lines = ''.join(lines[7:])
print(lines)


# Вам доступен текстовый файл lines.txt из нескольких строк. Напишите программу, которая выводит на экран
# случайную строку из этого файла.
# import random
# with open('lines.txt', encoding='utf-8') as file:
#     content = file.readlines()
#     print(content[random.randint(0, len(content) - 1)])


# Вам доступен текстовый файл numbers.txt из двух строк, в каждой из них записано целое число.
# Напишите программу, выводящую на экран сумму этих чисел.

# with open('numbers.txt', 'r', encoding='utf-8') as file:
#     num = file.readline()
#     total = 0
#     while num != '':
#         total += int(num.rstrip())
#         num = file.readline()
#     print(total)


# Вам доступен текстовый файл nums.txt. В файле записано два целых числа, они могут быть разделены символами
# пробела и конца строки. Напишите программу, выводящую на экран сумму этих чисел.

# with open('nums.txt', 'r', encoding='utf-8') as file:
#     num = file.read().split()
#     num_list = [int(item) for item in num]
#     print(sum(num_list))


# Вам доступен текстовый файл prices.txt с информацией о заказе из интернет-магазина.
# В нем каждая строка с помощью символа табуляции (\t) разделена на три колонки:
# 1. наименование товара;
# 2. количество товара (целое число);
# 3. цена (в рублях) товара за 1 шт. (целое число).
# Напишите программу, выводящую на экран общую стоимость заказа.

# with open('prices.txt', 'r', encoding='utf-8') as file:
#     line = file.readline()
#     total = 0
#     while line != '':
#         line = line.rstrip().split()
#         total += int(line[1]) * int(line[2])
#         line = file.readline()
#
# print(total)


# Вам доступен текстовый файл text.txt с одной строкой текста. Напишите программу,
# которая выводит на экран эту строку в обратном порядке.

# with open('text.txt', 'r', encoding='utf-8') as file:
#     line = file.readline()
#     print(line[::-1])


# Вам доступен текстовый файл data.txt, в котором записаны строки текста. Напишите программу,
# выводящую все строки данного файла в обратном порядке: сначала последнюю, затем предпоследнюю и т.д.

# with open('data.txt', 'r', encoding='utf-8') as file:
#     line_list = [item.rstrip() for item in file]
#     line_list.reverse()
#     print(*line_list, sep='\n')


