# Написание программы, в которой реализуется функция проверки надежности введенного пользователем пароля.
# Ответ программы может быть лишь “отвечает/не отвечает требованиям”.
# 	Сами требования:
# - длина от 10 символов,
# - содержит в себе минимум 2 цифры.

# объявляем функцию
def check_symbols(password):
    import re

    symbol_pattern = "[0-9]"
    symbol_found = re.findall(symbol_pattern, password)
    return len(symbol_found) >= 2 and len(password) >= 10

# исходные данные
password = input()

if check_symbols(password):
    print(f'Пароль {password} достаточно надежен!')
else:
    print(f'Пароль {password} недостаточно надежен!')