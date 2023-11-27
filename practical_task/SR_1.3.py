import re
import random

def generate_password():
    letters = "<>,*&^%$#@!-=+'abcdefghijklnopqrstuvwxyz1234567890"
    value = ''
    for i in range(12):
        value += random.choice(letters)
    return value

def check_symbols(passw):
    symbol_pattern = "[<>,*&^%$#@!-=+'0-9]"
    symbol_found = re.findall(symbol_pattern, passw)
    return len(symbol_found) >= 3 and len(passw) >= 10

password = input('Введите пароль для проверки: ')

if check_symbols(password):
    print(f'Пароль {password} достаточно надежен!')
else:
    print(f'Пароль {password} недостаточно надежен. Лучше используйте {generate_password()}')
