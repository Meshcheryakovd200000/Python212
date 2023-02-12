# def get_sum(a, b, c=0, d=1):
#     return a + b + c + d
#
# print(get_sum(1, 5, 2, 7))
# print(get_sum(1, 5, 2))
# print(get_sum(1, 5))
# print(get_sum(1, 5, d=2))

# --------------------------
# def set_param(c=20, s="-"):
#     for i in range(c):
#         print(s, end="")
#     print()
#
# set_param(10, s="+")
# set_param(5, "*")
# set_param(7)
# ----------------------------

# video 15 para 19 minut

# def digits_sum(n, even=True):  # 9874023
#     s = 0
#     while n > 0:  # 0
#         num = n % 10  # 9
#         if even and num % 2 == 0:
#             s += num  # 2 + 0 + 4 + 8
#         if not even and num % 2 != 0:
#             print(even)
#             s += num
#         n //= 10  # 0
#     return s
#
#
# print("Сумма чётных цифр:")
# print(digits_sum(9874023))
# print(digits_sum(38271))
# print(digits_sum(123456789))
#
# print("Сумма нечетных цифр:")
# print(digits_sum(9874023, even=False))
# print(digits_sum(38271, even=False))
# print(digits_sum(123456789, even=False))

# ---------------------------------------------
# video 15 para, 40 minut

# def display_info(name, age):
#     print("Name:", name, "\nAge:", age)
#
#
# display_info("Ira", 23)
# display_info(23, "Ira")
# display_info(age=23, name="Ira")

# --------------------------------------

# списки - изменяемые типы данных, а строки - неизменяемые  и числовой - и вещественный - и булевый(логический) - тип
# данных неизменяемый !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# lt1 = [1, 2, 3]
# lt2 = [1, 2, 3]
# print(id(lt1))
# print(id(lt2))
#
# print(lt1 == lt2)
# print(lt1 is lt2)
#
# a = True  # 'Hello', 3, 3.3
# b = True  # 'Hello', 3, 3.3
# print(id(a))
# print(id(b))
#
# print(a == b)
# print(a is b)

# s = "Hello"
# print(s, id(s))
# s = s + "World"
# print(s, id(s))
#
# a = 5
# print(a, id(a))
# a += 1
# print(a, id(a))
#
# s = "Hello"
# print(s, id(s))
# s = s[1:-1]
# print(s, id(s))

# -----------------------
# def add_number(n):
#     print("Внутри функции:", n, id(n))
#     n += 1
#     print("Измененное значение:", n, id(n))
#     return n
#
#
# x = 1
# print("До функции:", x, id(x))
# m = add_number(x)
# print("После функции:", m, id(m))

# --------------------------------

# def add_number(n):
#     print("Внутри функции:", n, id(n))
#     n = n + [4]  # n += [4]
#     print("Измененное значение:", n, id(n))
#
#
# x = [1, 2, 3]
# print("До функции:", x, id(x))
# add_number(x)
# print("После функции:", x, id(x))


# Кортеж (tuple)!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Kortez - neizmenyaemii tip dannih
# video 16 para

# lst = [10, 20, 30]  # spisok
# tpl = (10, 20, 30)  # kortez (кортеж)
# print(lst)
# print(tpl)
# print(lst.__sizeof__())
# print(tpl.__sizeof__())

# !!! spisok zanimaet bolshe pamyati chem kortez

# a = ()
# print(type(a))
# b = tuple()
# print(type(b))
#
# a = (1, 2, 3, 4, 5)
# print(a, type(a))
# c = 1, 2, 3, 4, 5
# print(type(c))
# b = tuple(c)
# print(b, type(b))
#
# t = (2,)
# print(type(t))

# a = (1, 2, 3, 4, 5)
# print(a)
# print(a[3])
# print(a[1:3])
# # a[3] = 55
# # print(a)

# s = ([int(input("-> ")) for i in range(2)])  # spisok
# print(type(s))
# s = tuple(int(input("-> ")) for i in range(3))  # kortez(tuple)
# print(type(s))

# from random import randint

# s = [randint(1, 20) for i in range(10)]  # spisok
# print(type(s))
#
# a = tuple(randint(1, 20) for i in range(10))  # kortez
# print("kortez 'a' ", type(a))


# video 16 para 20 minut

# Заполнить кортеж из 10 элементов степенями двойки от 1 до 12  (2, 4, 8, 16.....)

# s = tuple(2 ** i for i in range(1, 13))
# print(s)

# t1 = tuple("hello")
# t2 = tuple("world")
# t3 = t1 + t2
# print(t3)


# print(len(t3))
# print(t3.count('l'))
# print(t3.count('a'))
# print(t3.index('l', 4))
#
# if 'w' in t3:
#     print(t3.index('w'))
# else:
#     print("Такого символа нет")

# for i in range(len(t3)):
#     # t3[i] = t3[i] * 2  # элементы кортежа изменять нельзя
#     print(t3[i] * 2, end=" ")
# print("\n", t3)

# video 16 para 31 minuta

# def slicer(tpl, el):  # tpl - tuple and el - элемент в кортеже
#     if el in tpl:
#         if tpl.count(el) > 1:
#             # pass  - пока нет кода, пропуск
#             # return tpl[tpl.index(el):tpl.index(el, tpl.index(el) + 1) + 1]
#             start = tpl.index(el)
#             second = tpl.index(el, tpl.index(el) + 1)  # +1 чтобы 8 засчитывалась
#             return tpl[start:second +1]
#         else:
#             return tpl[tpl.index(el):]  # срез, возвращает в кортеже от 8ого элемента до конца
#     else:
#         return ()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))

# video 16 para 49 minuta

# from random import randint
#
#
# def tuple_func(start, end):
#     return tuple(randint(start, end) for _ in range(10))
#
#
# tuple_1 = tuple_func(0, 5)
# tuple_2 = tuple_func(-5, 0)
# tuple_3 = tuple_1 + tuple_2
# count_0 = tuple_3.count(0)
#
# print(tuple_1)
# print(tuple_2)
# print(tuple_3)
# print('Count 0: ', count_0)

# t = (10, "Hello", [1, 2, 3], (4, 5, 6), ["hello", "world"])
# print(t, id(t))
# t[-1][0] = 'new'  # poslednii index korteja поменяем nulevoi index
# print(t, id(t))
# t[4].append('hi')  # dobavili v spisok element 'hi' - (4ый element korteja)
# print(t, id(t))  # sam kortej ne pomenyalsya vidno po id

# t = (1, 2, 3)
# # x = t[0]
# # y = t[1]
# # z = t[2]
# x, y, z = t  # raspakovka korteja v Python a v java script - eto nazivaetsya - distrukturizaciya
# print(x, y, z)

# def get_user():
#     name = "Tom"
#     age = 22
#     is_married = False
#     return name, age, is_married  # esli function vozvrashaet bolshe odnogo znacheniya
#     # to ona vozvrashaet type dannix 'tuple'(kortej) s neskolkimi znacheniyami
#     # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#
#
# # user = get_user()
# # print(user)
# # name1, age1, is_married1 = user
# # print(user[0])
# # print(user[1])
# # print(user[2])
# # print(name1, age1, is_married1)
#
# name2, age2, is_married2 = get_user()
# print(name2, age2, is_married2)
