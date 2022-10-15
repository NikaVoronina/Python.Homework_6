# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ]

# Было:

# n = int(input('Введите число: '))
# factorial = 1
# for i in range(1, n + 1):
#     factorial *= i
#     print(factorial, end = ' ')

# Стало:

n = int(input('Введите число: '))
factorial = lambda a, b: a * b
f = 1
for i in range(n):
    i += 1
    f = factorial(f, i)
    print(f, end = ' ')

