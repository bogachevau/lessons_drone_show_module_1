# s = input('Введите строку для проверки: ')
# sym = input("Введите символ для поиска: ")
# s_list = list(s)
# count = 0
# for i in s_list:
#     if i == sym:
#         count +=1
# print(f'В строке символ {sym} найден {count} раз')

# a, b = float(input('Введите сторону прямоугольника а: ')), float(input('Введите сторону прямоугольника b: '))
# if a > 0 and b > 0:
#     P_sm = 2 * a + 2 * b
#     S_sm = a * b
#     print(f'Периметр прямоугольника равен {P_sm} см')
#     print(f'Площадь прямоугольника равна {S_sm} см2')
#     print(f'Периметр прямоугольника равен {P_sm * 10} мм')
#     print(f'Площадь прямоугольника равна {S_sm * 100} мм2')
# else:
#     print('Введены некорректные данные')

# На вход программе подается строка генетического кода, состоящая из букв А (аденин), Г (гуанин), Ц (цитозин),
# Т (тимин). Напишите программу, которая подсчитывает сколько аденина, гуанина, цитозина и
# тимина входит в данную строку генетического кода.
# s = input()
# print(f'аденин: {s.lower().count("а")}')
# print(f'гуанин: {s.lower().count("г")}')
# print(f'цитозин: {s.lower().count("ц")}')
# print(f'тимин: {s.lower().count("т")}')

# На вход программе подается строка текста. Напишите программу, которая подсчитывает количество цифр в данной строке.
# s = input()
# count = 0
# for i in range(len(s)):
#     if s[i] in '1234567890':
#         count +=1
# print(count)