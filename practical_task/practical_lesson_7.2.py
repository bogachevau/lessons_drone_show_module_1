# Напишите программу определяющую площадь круга и длину окружности по заданному радиусу R

# from math import *
# def calculate_S_circle(r):
#     S = pi * pow(r, 2)
#     print(f'Площадь круга равна: {round(S, 3)} при радиусе равном {r}')
#
# def calculate_C_circle(r):
#     C = 2 * pi * r
#     print(f'Длина окружности равна: {round(C, 3)} при радиусе равном {r}')
#
# R = float(input('Введите значение радиуса: '))
# calculate_S_circle(R)
# calculate_C_circle(R)


# Даны три вещественных числа a, b, c. Напишите программу, которая находит вещественные корни квадратного уравнения.
# ax2+bx+c=0. Если уравнение имеет два корня, то следует вывести их в порядке возрастания.

# from math import *
# def calc_quad_eq(a, b, c):
#     D = b ** 2 - 4 * a *c
#     if D > 0:
#         x1 = (-b - sqrt(D)) / (2 * a)
#         x2 = (-b + sqrt(D)) / (2 * a)
#         print(f'x1 = {min(x1, x2)}')
#         print(f'x2 = {max(x1, x2)}')
#     elif D == 0:
#         print(f'x = {-(b / (2 * a))}')
#     else:
#         print('Корней нет')
#
# a, b, c = float(input()), float(input()), float(input())
# calc_quad_eq(a, b, c)


# Площадь правильного многоугольника с длиной стороны a и количеством сторон n вычисляется по формуле
# import math
# def calc_multi(a, n):
#     S = (n * a) / (4 * math.tan(math.pi / n))
#     print(f'Площадь правильного многоугольника с длиной стороны {a} и количеством сторон {n} = {S}')
#
# a = float(input('Введите длину стороны многоугольника: '))
# n = int(input('Введите количество сторон многоугольника: '))
# calc_multi(a, n)

# Напишите функцию для декодирования шифра Цезаря.
def code_caesar(n, s):
    temp = 0
    for i in range(len(s)):
        temp = ord(s[i]) - n
        if temp < 97:
            temp += 26
        print(chr(temp), end='')

n, s = int(input()), input()
code_caesar(n, s)