# video 13 para 24 minuta

import math as m
# #
# num1 = m.ceil(3.2)  # okruglenie v bolsuyu storonu
# num2 = m.floor(3.8)  # okruglenie v niznuyu storonu
# num3 = m.sqrt(2)  # okruglenie v niznuyu storonu
# print(num1)
# print(num2)
# print(num3)
# # print(math.pi)

# from math import pi
#
# # num1 = pi(3.2)
# # print(num1)
#
# # Vvodim radius okruznosti. Naiti dlinu okruznosti
#
# r = int(input("Ввести радиус окружности: "))
# print("Длина окружности: ", round(2 * pi * r, 2))

# moduli data and time

# import time

# second = time.time()
# print(second)
# a = 72284021
# local_time = time.ctime(a)
# print(local_time)
# res = time.localtime()
# print(res)
# print(res.tm_mon, res.tm_year)
# print(time.strftime("Today is %B %d, %Y"))
# print(time.strftime("%d/%m/%Y, %H:%M:%S", time.localtime(a)))

# pause = 1
# print("Запуск программы")
# time.sleep(pause)
# print(pause, "сек.")

# --------------------- video 13 para 1 час 10 минут
# text = input("Название напоминания: ")  # Задача решена
# local_time = float(input("Через сколько минут: "))
# local_time = local_time * 60
# time.sleep(local_time)
# print(text)

# -------------------------

# start = time.time()
# time.sleep(5)
# finish = time.time()
# res = finish - start
# print(res)

# -------------------------

# start = time.monotonic()
# time.sleep(5)
# finish = time.monotonic()
# res = finish - start
# print(res)

# import locale
#
# locale.setlocale(locale.LC_ALL, "ru")
#
# print(time.strftime("Сегодня %B %d, %Y"))

# video 14 para


# Функции !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Function

# def hello(name, age):
#     print("Hello, ", name, ". I am ", age, sep="")
#
#
# hello("Irina", 20)
# hello("Ivan", 26)

# def get_sum(a, b):
#     print(a + b)
#
#
# x = 2
# y = 5
# get_sum(x, y)
# get_sum('abc', 'hello')
# get_sum(2.5, 4.3)

# ------------------------
# video 14para 16 minut

# 1 variant:
# def func(n, a, b):
#     for i in range(n):
#         if i % 2:
#             print(b, end='')
#         else:
#             print(a, end='')
#     print()
#
#
# func(9, "+", "-")
# func(7, "X", "0")
#
#
# # 2 variant
# def func2(n, a, b):
#     [print(b, end='') if i % 2 else print(a, end='') for i in range(n)]
#     print()
#
#
# func2(9, "+", "-")
# func2(7, "X", "0")

# 3 variant:
# def func3(n, a, b):
#     for i in range(n):
#         print(a, end="")
#         a, b = b, a
#     print()
#
#
# func3(9, "+", "-")
# func3(7, "X", "0")

# --------------------------------

# video 14 para 30 minut

# def get_sum(a, b):
#     if a > b:
#         return True
#     else:
#         return False
#
#
# x = 15
# y = 7
# if get_sum(x, y):
#     print(x, "больше", y)
# else:
#     print(y, "больше", x)

# ------------------------------
# video 14 para 42 minut

# a = int(input("Введите 1 целое число: "))
# b = int(input("Введите 2 целое число: "))
#
# def min_sum(a, b):
#     if a > b:
#         print("1 > 2 тогда первое - второе число: ", a - b)
#     else:
#         print("2 > 1 тогда первое + второе число: ", a + b)
#
#
# min_sum(a, b)
# ------------------------------

# video 14 para 46 minut

# def cube(a):
#     return a * a * a
#
#
# for i in range(1, 11):
#     print(i, "в кубе =", cube(i))


# ---------------------------
# 1 способ:

# def change(lst):
#     lst[-1], lst[0] = lst[0], lst[-1]
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(["с", "л", "о", "н"]))


# 2 способ:

# def change(lst):
#     n = lst.pop()
#     m = lst.pop(0)
#     lst.insert(0, n)
#     lst.append(m)
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(["с", "л", "о", "н"]))

# --------------------------------

# Proverka nadeznosti parolya

# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#
#     for ch in password:
#         if "A" <= ch <= "Z":
#             has_upper = True
#         if 'a' <= ch <= 'z':
#             has_lower = True
#         if '0' <= ch <= '9':
#             has_num = True
#
#     if len(password) >= 8 and has_upper and has_num and has_lower:
#         return True
#     return False
#
#
# p = input("Введите пароль: ")
# if check_password(p):
#     print("Это надежный пароль.")
# else:
#     print("Это ненадежный пароль")

# -------------------------
# print(5 / -3)
# print(5 // -3)
# print()
# print(5 / 3)
# print(5 // 3)
