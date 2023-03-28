# video 21 para

# parallelnaya obrabotka 2ux slovarey, 10 minuta

# dict_one = {'name': 'Igor', 'last_name': 'Doe', 'job': 'Consultant'}
# dict_two = {'name': 'Irina', 'last_name': 'Smith', 'job': 'Manager'}
#
# for (k1, v1), (k2, v2) in zip(dict_one.items(), dict_two.items()):
#     print(k1, v1)
#     print(k2, v2)

# -----------------

# iz spiska Tuple soberem v dict

# pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
# # print(dict(pairs))
# a, b = zip(*pairs)
# print(a)
# print(b)
# ---------------

# letters = ['b', 'a', 'd', 'c']
# numbers = [3, 1, 2, 4]
# data = list(zip(letters, numbers))
# print(data)
# data.sort()
# print(data)
# data1 = list(zip(numbers, letters))
# data1.sort()
# print(data1)
# data2 = dict(data1)
# print(data2)
# data3 = sorted(data2.items())
# print(data3)

# ----------------------

# one = {'apple': 0.4, 'orange': 0.35, 'pepper': 0.5}
# two = {'pepper': 0.2, 'onion': 0.55}
#
# print({**two, **one})  # raspakovka slovarya (объединение словарей)
#
# for k, v in {**two, **one}.items():
#     print(k, "->", v)

# kak proishodit raspakovka:
# {
#     'apple': 0.4, 'orange': 0.35,
#     'pepper': 0.2, 'onion': 0.55
# }

# ----------------
# video 21 para, 40 minut
# data = [2, 5, 3, 4, 1, 5]
# for i in data:
#     print(i, end=" ")
# print()
# for i in range(6):
#     print(i, end=" ")
# print()
# colors = ['red', 'green', 'blue']
# i = 1
# for color in colors:
#     print(i, ") ", color, sep="")
#     i += 1

# enumerate()  (video 21, 48 minuts)

# colors = ['red', 'green', 'blue']
# for num, val in enumerate(colors, 1):  # numeraciya nachinaetsya s 1
#     print(num, ") ", val, sep="")

# enumerate() - rabota so slovarem:
# n = {i: i + 2 for i in range(10, 18)}
# print(n)
#
# for i, (j, v) in enumerate(n.items(), 100):
#     print(i, ": ", j, " -> ", v, sep="")

# a = [1, 2, 3]
# b = [*a, 4, 5, 6]
# print(b)

# def func(*args):
#     res = 0
#     for i in args:
#         res += i
#     return res
#
#
# print(func(2, 3, 4, 5, 1))
# print(func(2, 4, 7))
# print(func())

# -----------------
# Napisat def kotoraya prinimaet proizvolnoe kolichestvo argument and vozvrashaet dict,
# v kotorom kazdii element spiska yavlyaetsya and key and znacheniem.

# def to_dict(*lst):
#     return {i: i for i in lst}
#
#
# print(to_dict(1, 2, 3, 4))
# print(to_dict('gray', (2, 17), 3.11, -4))
# ---------------------

# Napisat def kotoraya prinimaet proizvolnoe chislo chisel, vichislyaet ix sredne arifmeticheskoe and
# vozvrashaet tolko te chisla, kotorie menshe poluchennogo srednego arifmeticheskogo.

# def func(*lst):
#     res = 0
#     for i in lst:
#         res += i
#     res = res / i
#     # res = sum(lst) / len(lst)
#     print(res)
#     s = []
#     for j in lst:
#         if j < res:
#             s.append(j)
#     return s
#
#
# print(func(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(func(3, 6, 1, 9, 5))

# ---------------------

# video 22

# def and args (функции и аргументы)

# def func(a, *args):
#     return a, args
#
#
# print(func(1))
# print(func(1, 2, 3, 'abc'))

# def print_scores(student, *scores):  # * -zvezdochka eto luboe kol-vo znachenii !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#     print("Student Name:", student)
#     for score in scores:
#         print(score, end=" ")
#     print()
#
#
# print_scores("Джонатан", 100, 95, 88, 92, 99)
# print_scores("Роман", 96, 20, 33)

# def func(**kwargs):  # kwargs - nabor key and values !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#     return kwargs
#
#
# print(func(a=1, b=2, c=3))
# print(func())
# print(func(d="python"))

# ---------------------------
# video 22 para 9 minuts

# def db(**data):
#     my_dict.update(data)
#
#
# my_dict = {'one': 'first'}
# db(k1=22, k2=31, k3=11, k4=91)
# db(name='Bob', age=31, weight=61, eyes_color='gray')
# print(my_dict)


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# video 22para 20 minuta, зачения и кортеж и словарь в функции

# def func(aa, *args, d=0, **kwargs):
#     return aa, args, d, kwargs
#
#
# print(func("one", 5, 9, 7, 8, 1, a=1, d=6, b=2, c=3))

# Области видимости (Oblasti vidimosti) 4 oblasti !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 1)globalnaya peremennaya, 2)localnaya, 3)Enclosed, 4)builtin
# name = "Tom"  # globalnaya peremennaya
#
#
# def hi():
#     global name
#     name = "Sam"  # localnaya peremennaya
#     surname = "Johnson"
#     print("Hello", name, surname)
#
#
# def bye():
#     print("Good bye", name)
#
#
# print(name)
# hi()
# bye()
# print(name)

# -----------------
# i = 5
# arg = 5
#
#
# def func(arg=i):
#     print(arg)
#
#
# i = 6
# arg = 6
# func()  # 5
# func(arg)  # 6
# -------------------

# x = 7
#
#
# def add_five(a):
#     x = 2  # Enclosed
#
#     def add_two():
#         return a + x
#
#     return add_two()
#
#
# print(add_five(3))
# ----------------------

# import builtins
#
# name = dir(builtins)  # builtin
#
# for t in name:
#     print(t)
# ------------------
# min = [5, 6, 8, 9, 7]
# print(min(min))  # нельзя называть переменную которая уже есть встроенная функция в python
# min1 = [5, 6, 8, 9, 7]
# print(max(min1))
# a = [5, 6, 7, 8, 8]
# print(min(a))
# ------------------

# детальное рассмотрение вложенных функций
# video 22 para 53 minuta

# def outer_func(who):
#     def inner_func():
#         print("Hello,", who)
#
#     inner_func()
#
#
# outer_func('World!')

# def fun1():
#     a = 6
#
#     def fun2(b):
#         a = 4
#         print("a + b =", a + b)
#
#     print("a =", a)
#     fun2(4)
#
#
# fun1()
# ------------------

# x = 25
#
#
# def fn():
#     global t
#     a = 30  # 35
#
#     def inner():
#         nonlocal a
#         a = 35
#         print("nonlocal:", a)
#
#     inner()
#     t = a
#
#
# fn()
#
# z = x + t  # 25 + 30 = 55  а когда объявили nonlocal a,  то a стала равна 35
# print(z)
# ----------------

def fn1():
    x = 25

    def fn2():
        x = 33

        def fn3():
            nonlocal x
            x = 55

        fn3()
        print('fn2.x =', x)

    fn2()
    print('fn1.x =', x)


fn1()
