# Задание 1
# name = input('Введите имя файла: ')
# try:
#     with open(name, 'r', encoding='utf-8') as file:
#         lines = 0
#         words = 0
#         for line in file:
#             lines += 1
#             words += len(line.split())
#         print(f'В файле {name}: {lines} строк и {words} слов')
# except FileNotFoundError:
#     print('Такого файла не найдено. Проверьте правильность написания имени файла')


# Задание 2
name_input = input('Введите название копируемого файла: ')
name_output = input('Введите имя файла для копии: ')

try:
    with open(name_input, 'r', encoding='utf-8') as file_input:
        text = file_input.read()
    file_output = open(name_output, 'w', encoding='utf-8')
    file_output.write(text)
    file_output.close()
    print(f'Копирование из файла {name_input} в файл {name_output} завершено успешно')
except FileNotFoundError:
    print('Такого файла не найдено. Проверьте правильность написания имени файла')