# Python, 09.02.2023, 39 пара main20

# ------------------------------------------------------------------------------------------------------------------
# Алгоритмы сортировки
# ------------------------------------------------------------------------------------------------------------------
# video 38 пара 01час:00минут

# -----------------------------------------------------------------------------------------------------------------
# "Пузырьковая сортировка"

# homework19_python - разбираем домашнее задание

from random import randint
import time

# def bubble(array):
#     for i in range(len(array) - 1):
#         for j in range(len(array) - i - 1):
#             if array[j] > array[j + 1]:  # сортировка по возрастанию, если знак поменять на < то будет по убыванию
#                 array[j], array[j + 1] = array[j + 1], array[j]
#
#
# a = [randint(1, 100) for i in range(10000)]
#
# # print(a)
# start = time.monotonic()  # monotonic() - показывает более точное время в секундах
# bubble(a)
# # print(a)
# res = time.monotonic() - start
# print(round(res, 3), "sec")

# ---------------------------

# video 39 пара 26 минут
# -------------------------------------------------------------------------------------------------------------------
# Сортировка слиянием

# def merge_sort(a):
#     n = len(a)
#     if n < 2:
#         return a
#
#     left = merge_sort(a[:n // 2])
#     right = merge_sort(a[n // 2:n])
#
#     i = j = 0
#     res = []
#
#     while i < len(left) or j < len(right):
#         if not i < len(left):
#             res.append(right[j])
#             j += 1
#         elif not j < len(right):
#             res.append(left[i])
#             i += 1
#         elif left[i] < right[j]:
#             res.append(left[i])
#             i += 1
#         else:
#             res.append(right[j])
#             j += 1
#     return res
#
#
# array = [randint(1, 100) for i in range(10000)]
# # print(array)
# start = time.monotonic()
# array = merge_sort(array)
# # print(array)
# res = time.monotonic() - start
# print(round(res, 3), "sec")

# --------------------------------------------------------------------------------------------------------------------
# Сортировка Шелла
# video 39 пара 01час: 01 минута

# def shell_sort(s):
#     gap = len(s)
#
#     while gap > 0:
#         for val in range(gap, len(s)):
#             cur_val = s[val]
#             pos = val
#
#             while pos >= gap and s[pos - gap] > cur_val:
#                 s[pos] = s[pos - gap]
#                 pos -= gap
#                 s[pos] = cur_val
#
#         gap //= 2
#     return s
#
#
# a = [randint(1, 100) for i in range(10000)]
# # print(a)
# start = time.monotonic()
# shell_sort(a)
# # print(a)
# res = time.monotonic() - start
# print(round(res, 3), "sec")

# -------------------------------------------------------------------------------------------------------------------
# Быстрая сортировка

# video 40, 3 minuta

# def quick_sort(a):
#     if len(a) > 1:
#         x = a[(len(a) - 1) // 2]
#         low = [i for i in a if i < x]  # в low попало все что меньше 0
#         eq = [i for i in a if i == x]  # среднее значение
#         hi = [i for i in a if i > x]  # в hi попадает все что больше 0
#         a = quick_sort(low) + eq + quick_sort(hi)
#     return a
#
#
# # lst = [-4, 2, 7, 0, 1, 10, -3]
# lst = [randint(1, 100) for i in range(10)]
# print(lst)
# start = time.monotonic()
# lst = quick_sort(lst)
# print(lst)
# lst.sort()
# res = time.monotonic() - start
# print(res, "sec")

# -------------------------------------------------------------------------------------------------------------------
# Файлы
# -------------------------------------------------------------------------------------------------------------------
# video 40 пара main20, 24 минута

# f = open(r'D:\Python212\Python\work_python\20python_сортировки_файлы\text.txt')  # открываем файл
# # f = open('D:\\Python212\\Python\\work_python\\20python_сортировки_файлы\\text.txt')  #открываем файл "абсолютный путь"
# print(f)
# print(*f)  # * - чтобы посмотреть что внутри файла
# print(f.mode)  # в каком режиме файл чтение -r или запись -w
# print(f.name)  # имя файла
# print(f.encoding)  #  кодировка файла
# f.close()  # закрываем файл
# print(f.closed)  # проверяем закрылся ли файл, если закрылся то покажет - True


# f = open('text.txt', 'r')  # открываем файл "относительный путь"
# print(f.read(3))
# print(f.read())
# f.close()

# f = open('text.txt', 'r')  # открываем файл "относительный путь"
# print(f.readline())
# print(f.readline(8))
# print(f.readline())
# print(f.readline())
# f.close()


# f = open('text.txt', 'r')  # открываем файл "относительный путь"
# print(f.readlines(16))
# print(f.readlines())
#
# f.close()

# f = open('text.txt', 'r')  # открываем файл "относительный путь"
# for line in f:
#     print(line)
#
# f.close()
# ---

# Задача: определите количество строк в файле

# 1
# lines = 0
# f = open('text.txt', 'r')  # открываем файл "относительный путь"
# for line in f:
#     lines += 1
# print(lines)
# f.close()
#
# # 2
# fail = open('text.txt')
# count_lines = len(fail.readlines())
# print(count_lines)

# ---

# f = open('xyz.txt', 'w')  # f = open('xyz.txt', 'w', encoding="utf-8")
# f.write('Hello\nWorld')  # f.write('Hello\nWorld'.center(12, "="))
# f.close()

# ---

# f = open('xyz.txt', 'a')  # режим "а" это - дозапись
# # f.write('Hello\nWorld')  #
# # lines = ['This is line 1', 'This is line 2']
# lines = [str(i ** 5) for i in range(1, 20)]
# print(lines)
# # f.writelines(lines)
# for index in lines:
#     f.write(index + "\t")
# f.close()

# ---

# Задача: Замените строку в текстовом файле
# Тест:
# Замена строки в текстовом файле;
# Изменить строку в списке;
# Записать список в файл;
#
# Замена строки в текстовом файле;
# Hello world!
# Записать список в файл;

f = open("text2.txt", "w")
f.write("Замена строки в текстовом файле;\nИзменить строку в списке;\nЗаписать список в файл;")
f.close()

f = open("text2.txt", "r")
read_f = f.readlines()
print(read_f)
for i in range(len(read_f)):
    if read_f[i] == "Изменить строку в списке;\n":
        read_f[i] = "Hello World!\n"
print(read_f)
f.close()

f = open("text2.txt", "w")
f.writelines(read_f)
f.close()
