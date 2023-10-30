# a, b, h = (float(input('Введите длину первого основания ')), float(input('Введите длину 2-го основания ')),
#            float(input('Введите высоту трапеции ')))
# S = ((a + b) / 2) * h
# print('Площадь трапеции равна', S)

# num = int(input('Введите трех значное число: '))
# last_digit = num % 10
# two_digit = (num // 10) % 10
# first_digit = num // 100
# print(first_digit, two_digit, last_digit, sep='\n')

a, b = int(input()), int(input())
y = 3 * (a + b) ** 3 + 275 * b ** 2 - 127 * a - 41
print(y)