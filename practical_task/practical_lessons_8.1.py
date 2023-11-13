import random

def generate_password():
    letters = 'abcdefghijklnopqrstuvwxyz1234567890'
    value = ''
    for i in range(12):
        value += random.choice(letters)
    print(value)

generate_password()
