# n = int(input())
# for _ in range(n):
#     print('*' * 19)

# s = input()
# for i in range(1, 11):
#     print(f'{i} - {s}')

# n = int(input())
# for i in range(n + 1):
#     # print(f'Квадрат числа {i} равен {i ** 2}')
#     print('Квадрат числа', i, 'равен', i ** 2)

# n, m = int(input()), int(input())
# if m < n:
#     for m in range(m, n + 1):
#         print(m)
# elif m > n:
#     for m in range(m, n - 1, -1):
#         print(m)
# else:
#     print(m)

#Дано натуральное число. Напишите программу, которая вычисляет:
# - сумму его цифр;
# - количество цифр в нем;
# - произведение его цифр;
# - среднее арифметическое его цифр;
# - его первую цифру;
# - сумму его первой и последней цифры.

# num = int(input())
# n = num
# temp = 0
# total = 0
# count = 0
# multi = 1
# while num != 0:
#     temp = num % 10
#     total += temp
#     count += 1
#     multi *= temp
#     num = num // 10
# print(f'Сумма цифр равна {total}')
# print(f'Количество цифр {count}')
# print(f'Произведение цифр равно {multi}')
# print(f'Среднее арифметическое - {total / count}')
# print(f'Первая цифра - {temp}')
# print(f'Сумма первой и последней цифр {temp + n % 10}')

#На вход программе подается натуральное число n. Напишите программу, которая выводит числа от 1 до n включительно
# за исключением:
# чисел от 5 до 9 включительно;
# чисел от 17 до 37 включительно;
# чисел от 78 до 87 включительно.

# n = int(input())
# for i in range(1, n + 1):
#     if 5 <= i <= 9 or 17 <= i <= 37 or 78 <= i <= 87:
#         continue
#     print(i, end=' ')


#Дано натуральное число n (n≤ 9). Напишите программу, которая печатает таблицу размером n х 5, где в i-ой строке
# указано число i (числа отделены одним пробелом)

# n = int(input())
# for i in range(n):
#     for j in range(5):
#         print(i, end=' ')
#     print()

# s = 'Hello world!'
# print(s[0])
# print(s[:5])
# print(s[5:])
# print(s[1::2])
# print(s[::-1])
#
# if 'w' in s:
#     print('YES')
# else:
#     print('NO')

my_list = [1, 2, 3, 5, 10, 12, 15, 2.5, 3.5, '500', 'string']
total = 0
for i in range(len(my_list)):
    if type(my_list[i]) == int:
        total += my_list[i]
    else:
        print(f'Найден элемент {my_list[i]} неверного типа')
print(f'Сумма целочисленных элементов списка равна {total}')





