# video 37 пара main19
import re

# def to_str(n, base):  # base - основание системы счисления, n - число -254
#     convert = "0123456789ABCDEF"
#     if n < 0:
#         convert = convert[0] + convert[:0:-1] # 0FEDCBA987654321
#         # convert[:0:-1] - от начала до конца и разворачиваем в противоположную сторону
#         if n * (-1) < base:
#             return "-" + convert[n]
#         else:
#             return to_str((n // base) + 1, base) + convert[(n % base)]
#     else:
#         if n < base:
#             return convert[n]
#         else:
#             return to_str(n // base, base) + convert[n % base]
#             # -254/10=25


# отрицательные числа хранятся в дополнительном коде:
# https://ru.wikipedia.org/wiki/%D0%94%D0%BE%D0%BF%D0%BE%D0%BB%D0%BD%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9_
# %D0%BA%D0%BE%D0%B4
# print(to_str(-254, 10))
#
# print(int('FE', 16))

# ---

# def negative(a):
#     if not a:  # len(a) == 0 , a == []
#         return 0
#     else:
#         count = negative(a[1:])
#         if a[0] < 0:
#             count += 1
#         return count
#
#
# lst = [-2, 3, 8, -11, -4, 6]
# print(lst)
# n = negative(lst)
# print(n)  # 3

# ----

# Задача video Python 07.02.2023, 37 пара main 19, 27 minuts

# def validate_phone(number):
#     # ? - это одно повторение элемента или нету ниодного элемента
#     # * - это может быть много повторений элемента или нисколько, * -обычно для пробелов используется
#     # reg = r"^"  # от начала должны быть какие нибудь элементы
#     # reg = r"^\+?" # символ "+" может быть а может не быть
#     # reg = r"^\+?7"  # цифра 7
#     # reg = r"^\+?7\s*"  # пробел может быть а может не быть, добавляем - \s*
#     # reg = r"^\+?7\s*\(?"  # круглая скобка может быть а может не быть - \(?
#     # reg = r"^\+?7\s*\(?\d{3}"  # потом идут 3 цифры - \d{3}
#     # reg = r"^\+?7\s*\(?\d{3}\)?"  # круглая скобка может быть а может не быть - \)?
#     # reg = r"^\+?7\s*\(?\d{3}\)?\s*[\d\s-]"  # могут быть цифры - \d, могут быть пробелы \s, и может дефис "-"
#     # reg = r"^\+?7\s*\(?\d{3}\)?\s*[\d\s-]{7,9}"  # от 7 по 9 элементов отображалось
#     reg = r"^\+?7\s*\(?\d{3}\)?\s*[\d\s-]{7,9}$"  # $ - чтобы не было лишних элементов
#     # return re.search(reg, number).group()
#     return re.findall(reg, number)[0]
#
#
# print(validate_phone('+7 499 456-45-78'))
# print(validate_phone('+74994564578'))
# print(validate_phone('7 (499) 4564578'))
# print(validate_phone('7 (499) 456-45-78'))

# ----

# video python, 07.02.2023, 37 пара main 19, 37 minuta

# Рекурсивный обход вложенного списка.png

# names = ["Adam", ["Bob", ["Chet", "Cat", ["aaa"]], "Bard", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]
# # print(names[0])
# # print(names[1])
# # print(isinstance(names[0], list))
# # print(type(names[0]))
# # print(isinstance(names[1], list))
# # print(names[1][1][0])
# # print(isinstance(names[1][1][0], list))
# # print(len(names))
# print(names)
#
#
# # Задача посчитать колличество элементов в списке используя рекурсию. 46 minuta
#
# # def count_items(item_list):
# #     count = 0
# #     for item in item_list:
# #         if isinstance(item, list):
# #             count += count_items(item)
# #         else:
# #             count += 1
# #     return count
# #
# #
# # print("колличество элементов в списке: ", count_items(names))

# Задача посчитать колличество элементов в списке без рекурсии. 01:05 minuta, в следующий день разберем, этот
# код не совершенен:

# names = ["Adam", ["Bob", ["Chet", "Cat"], "Bard", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]
# print(names)
#
#
# def count_items(item_list):
#     count = 0
#     stack = []
#     current_list = item_list
#     i = 0
#     while True:
#         if i == len(current_list):
#             if current_list == item_list:
#                 return count
#             else:
#                 current_list, i = stack.pop()  # pop() - удаляет последний элемент из списка
#                 i += 1
#         if isinstance(current_list[i], list):
#             stack.append([current_list, i])
#             current_list = current_list[i]
#             i = 0
#         count += 1
#         i += 1
#
#
# print(count_items(names))

# Задача Выпрямление текущего списка, чтобы был без вложенных

# names = ["Adam", ["Bob", ["Chet", "Cat"], "Bard", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]
# print(names)
#
#
# def union(s):
#     if not s:  # если список не пустой
#         return s
#     if isinstance(s[0], list):
#         return union(s[0]) + union(s[1:])
#     return s[0:1] + union(s[1:])  # ["Adam"] + ["Adam"], ["Bob", Chet", "Cat"]
#
#
# print(union(names))

# Задача С помощью рекурсии удалить пробелы из строки

# def remove(text):  #
#     if not text:
#         return ""
#     if text[0] == "\t" or text[0] == " " or text[0] == "$":  # если в нулевом индексе табуляция или пробелы или $
#         # то переходит с 1ого инд.
#         return remove(text[1:])
#     else:
#         return text[0] + remove(text[1:])  # HelloWorld! + ''
#
#
# print(remove(" $Hello\tWorld$! "))

# --------------------------------------------------------------------------------------------------------------------
# Линейный (последовательный) поиск
# --------------------------------------------------------------------------------------------------------------------

# Задача Линейный поиск в неотсортированном списке:

# def seq_search(s, item):
#     pos = 0  # позиция индекса
#     found = False  #
#
#     while pos < len(s) and not found:
#         if s[pos] == item:
#             found = True
#         else:
#             pos += 1
#     return found
#
#
# lst = [54, 26, 93, 17, 77, 31, 44, 55, 20, 65]
# print(seq_search(lst, 93))  # True
# print(seq_search(lst, 28))  # False

# ---

# Задача Линейный поиск в отсортированном списке:

# def seq_search(s, item):
#     pos = 0  # 3
#     found = False  #
#     stop = False  # True
#     while pos < len(s) and not found and not stop:
#         if s[pos] == item:
#             found = True
#         else:
#             if s[pos] > item:
#                 stop = True
#             else:
#                 pos += 1
#     return found
#
#
# lst = [54, 26, 93, 17, 77, 31, 44, 55, 20, 65]
# lst.sort()  # [17, 20, 26, 31, 44, 54, 55, 65, 77, 93]
# print(lst)
# print(seq_search(lst, 93))  # True
# print(seq_search(lst, 28))  # False

# В отсортированном списке если элемента нет то он прекращает работу в этом примере до 31 > 28

# ----

# ---------------------------------------------------------------------------------------------------------------------
# Бинарный поиск
# поиск начинается с середины списка
# ---------------------------------------------------------------------------------------------------------------------

# def binary_search(s, item):
#     first = 0  # 0
#     last = len(s) - 1  # 0 - 1 = -1
#     found = False
#
#     while first <= last and not found:
#         midpoint = (first + last) // 2  # 3 // 2 = 1, поиск начинается с индекса 4, т.е. (9+0)/2 = целое 4
#         if s[midpoint] == item:
#             found = True
#         else:
#             if item < s[midpoint]:
#                 last = midpoint - 1
#             else:
#                 first = midpoint + 1
#
#     return found
#
#
# lst = [17, 20, 26, 31, 44, 54, 55, 65, 77, 93]
# print(binary_search(lst, 26))
# print(binary_search(lst, 28))

# ---------------------------------------

# ------------------------------------------------------------------------------------------------------------------
# Алгоритмы сортировки
# ------------------------------------------------------------------------------------------------------------------
# video 38 пара 01час:00минут

# "Пузырьковая сортировка"
from random import randint
import time


def bubble(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:  # сортировка по возрастанию, если знак поменять на < то будет по убыванию
                array[j], array[j + 1] = array[j + 1], array[j]


a = [randint(1, 100) for i in range(10000)]

# print(a)
start = time.monotonic()
bubble(a)
# print(a)
res = time.monotonic() - start
print(round(res, 3), "sec")
