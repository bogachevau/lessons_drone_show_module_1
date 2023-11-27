# Напишите функцию draw_box(), которая выводит звездный прямоугольник с размерами
# 14X10 в соответствии с образцом:
# **********
# *        *
# *        *
# *        *
# *        *
# *        *
# *        *
# *        *
# *        *
# **********

# объявление функции
# def draw_box():
#     print('*' * 10)
#     for _ in range(12):
#         print('*' + ' ' * 8 + '*')
#     print('*' * 10)
#
# # вызываем функцию
# draw_box()


# Напишите функцию draw_triangle(), которая выводит звездный прямоугольный треугольник с катетами,
# равными 10 в соответствии с образцом:
# *
# **
# ***
# ****
# *****
# ******
# *******
# ********
# *********
# **********

# объявление функции
# def draw_triangle():
#     for i in range(1, 11):
#         print('*' * i)
#
# # вызываем функцию
# draw_triangle()


# Напишите функцию draw_triangle(fill, base), которая принимает два параметра:
# fill – символ заполнитель;
# base – величина основания равнобедренного треугольника, должен быть нечетным;
# а затем выводит его.

# объявление функции
# def draw_triangle(fill, base):
#     centre = base // 2 + 1
#     count = 0
#     for i in range(1, base + 1):
#         if i > centre:
#             count -= 1
#         else:
#             count += 1
#         for _ in range(count):
#             print(fill, end='')
#         print()
#
# # считываем исходные данные
# fill, base = input('Введите символ заполнитель: '), int(input('Введите величину основания: '))
#
# # вызываем функцию
# draw_triangle(fill, base)


# Напишите функцию print_fio(name, surname, patronymic), которая принимает три параметра:
# name – имя человека;
# surname – фамилия человека;
# patronymic – отчество человека;
# а затем выводит на печать ФИО человека.

# объявление функции
# def print_fio(name, surname, patronymic):
#     list_fio = [surname[0], name[0], patronymic[0]]
#     print(*list_fio, sep='')
#
# # считываем исходные данные
# name, surname, patronymic = (input('Введите имя: ').title(), input('Введите фамилию: ').title(),
#                              input('Введите отчество: ').title())
#
# # вызываем функцию
# print_fio(name, surname, patronymic)


# На вход программе подается строка текста, содержащая имя, отчество и фамилию человека.
# Напишите функцию, которая выводит инициалы человека.

# объявление функции
def print_fio(s):
    list_fio = []
    for i in range(len(s)):
        temp_s = []
        temp_s.extend(s[i])
        list_fio.append(temp_s[0])
    st = '.'.join(list_fio)
    print(st, end='.')

# считываем исходные данные
s = input().split()

# вызываем функцию
print_fio(s)

