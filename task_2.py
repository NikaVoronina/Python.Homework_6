# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

# Было:

# num = input('Введите вещественное число: ')
# sum = 0
# for i in num:
#     if i != '.':
#         sum += int(i)
# print('Сумма цифр числа = ', sum)

# Стало:

num = input('Введите вещественное число: ')
sum = sum(map(int, num.replace('.', '')))
print('Сумма цифр числа = ', sum)