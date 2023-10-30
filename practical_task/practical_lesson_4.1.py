# if x > 0: # условие
#     print('Положительное число') # блок операторов 1
# else:
#     print('Отрицательное число') # блок операторов 2

# s = input()
# if s == 'Python':
#     print('Да')
# else:
#     print('Нет')

# numbers = int(input('Введите двузначное число '))
# first_digit = numbers // 10
# last_digit = numbers % 10
# if first_digit == last_digit:
#     print('YES')
# else:
#     print('NO')

# s1, s2 = input(), input()
# if s1 == s2:
#     print('Пароль принят')
# else:
#     print('Пароль не принят')

# num = int(input())
# if num % 2 == 0:
#     print('Четное число')
# else:
#     print('Не четное число')

# num = int(input('Введите четырехзначное число '))
# first_digit = num // 1000
# second_digit = (num // 100) % 10
# thrid_digit = (num % 100) // 10
# fourth_digit = num % 10
# if (first_digit + fourth_digit) == (second_digit - thrid_digit):
#     print('YES')
# else:
#     print('NO')

# a, b, c = int(input()), int(input()), int(input())
# if (c - b) + a == b:
#     print('YES')
# else:
#     print('NO')

# Напишите программу, которая по введённому возрасту пользователя сообщает, к какой возрастной группе он относится:
# до 13 включительно – детство;
# от 14 до 24 – молодость;
# от 25 до 59 – зрелость;
# от 60 – старость.

# age = int(input())
# if age <= 13:
#     print('детство')
# else:
#     if age <= 24:
#         print('молодость')
#     else:
#         if age <= 59:
#             print('зрелость')
#         else:
#             print('старость')

# if age <= 13:
#     print('детство')
# elif age <= 24:
#     print('молодость')
# elif age <= 59:
#     print('зрелость')
# else:
#     print('старость')

# Напишите программу, которая принимает три положительных числа и определяет, существует ли невырожденный
# треугольник с такими сторонами.
# Треугольник существует, если выполняется неравенство треугольника:
# a + b > c
# a + c > b
# b + c > a,
# где a, b, c - стороны треугольника.

# a, b, c = int(input()), int(input()), int(input())
# if a + b > c and a + c > b and b + c > a:
#     print('YES')
# else:
#     print('NO')

temp = float(input('Введите температуру: '))
unit = input('Введите единицы измерения температуры C/F: ')
if unit == 'C' or unit == 'c':
    c_to_f = 1.8 * temp + 32
    print(f'Температура {temp} С = {c_to_f} F')
elif unit == 'F' or unit == 'f':
    f_to_c = (temp - 32) / 1.8
    print(f'Температура {temp} F = {f_to_c} C')
else:
    print('Введено неверное значение')