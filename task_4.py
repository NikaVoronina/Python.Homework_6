# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# Было:

# list = [2, 3, 5, 6]
# result_list = []
# for i in range((len(list) + 1) // 2):
#     result_list.append(list[i] * list[len(list) - 1 - i])
# print(result_list)

# Стало:

import math
lst = list(map(int, input('Введите числа через пробел: ').split()))
print('Произведение пар чисел:', list([a * b for a, b in zip(lst[0:math.ceil(len(lst) / 2)], lst[::-1])]))
