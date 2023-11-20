# Напишите функцию is_prime(num), которая принимает в качестве аргумента натуральное число и возвращает значение
# True если число является простым и False в противном случае.

def is_prime(num):
    if num == 1:
        return False
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
        if count > 2:
            break
    return count == 2

n = int(input())

print(is_prime(n))