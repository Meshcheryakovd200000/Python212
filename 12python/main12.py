# video 23 para
# def outer(a1, b1, a2, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#
#     inner()
#     return [a, b]
#
#
# res = outer(2, 3, -1, 4)
# print(res)


# Замыкания!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# add1 = outer(5)
# print(add1(10))
#
# add2 = outer(6)
# print(add2(10))
#
# print(outer(7)(10))

# ---------------------
# def func1():
#     a = 1
#     b = 'line'
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a, b
#         c.append(4)
#         a = a + 1
#         b = b + "1"
#         return a, b, c
#
#     return func2
#
#
# func = func1()
# print(func())
# -------------------------

# def func(city):
#     s = 0
#
#     def func1():
#         nonlocal s
#         s += 1
#         print(city, s)
#
#     return func1
#
#
# res1 = func('Москва')
# res1()
# res1()
#
# res2 = func('Сочи')
# res2()
# res2()
#
# res1()

# ---------------------------

# students = {
#     'Alice': 98,
#     'Bob': 67,
#     'Chris': 85,
#     'David': 75,
#     'Ella': 54,
#     'Fiona': 35,
#     'Grace': 69
# }
#
#
# # Распределение студентов по баллам
# def make_classifier(lower, upper):
#     def classify_student(exam):
#         return {k: v for k, v in exam.items() if lower <= v < upper}
#
#     return classify_student
#
#
# A = make_classifier(80, 100)
# B = make_classifier(70, 90)
# C = make_classifier(50, 70)
# D = make_classifier(0, 50)
#
# print("A =", A(students))
# print("B =", B(students))
# print("C =", C(students))
# print("D", D(students))

# вложенные функции 2 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# video 23 para 45 minut
# def func(a, b):
#     def add():
#         return a + b
#
#     def sub():
#         return a - b
#
#     def mul():
#         return a * b
#
#     def replace():
#         pass
#
#     replace.add = add
#     replace.sub = sub
#     replace.mul = mul
#
#     return replace
#
#
# obj1 = func(5, 2)
# obj1()
# print(obj1.add())  # вызываем функцию add
# print(obj1.sub())  # вызываем функцию
# print(obj1.mul())  # вызываем функцию


# Lambda (анонимная функция) !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# video 23 para 51 minuta

# print((lambda x, y: x + y)(1, 2))  # function - Lambda
# print((lambda x, y: x + y)('a', 'b'))  # function - Lambda
# func = lambda x, y: x + y  # нежелательно присвоивать lambda функцию
#
# print(func(1, 2))
# print(func('a', 'b'))
#
#
# # тоже самое только через def=
# def summa(x, y):
#     return x + y
#
#
# print(sum(1, 2))
# print(summa('a', 'b'))

# ---------------------

# print((lambda x, y: x ** 2 + y ** 2)(2, 5))

# --------------------------


# s = lambda a=1, b=2, c=3: a + b + c
#
# print(s())
# print(s(10, 20, 30))
# ----------
# s = lambda *args: args
#
# print(s(1, 2, 3, 4))
# print(s(10, 20, 30))
# ----------
# f = (lambda x: x * 2,
#      lambda x: x * 3,
#      lambda x: x * 4)  # f - имя кортежа но внутри находится лямбда
#
# for i in f:
#     print(i('abc_'))
# --------------------------

# # def inc1(n):
# #     def add_two(x):
# #         return x + n
# #
# #     return add_two
# #
# #
# # def inc(n):
# #     return lambda x: x + n
# # --------------------------
#
# inc = (lambda n: lambda x: x + n)
#
# print(inc(42)(1))
# print(inc(42)(3))
# # f = inc(42)
# # print(f(1))
# # print(f(3))

# # ---------------
# # сумма трех принимаемых аргументов:
#
# sum3 = (lambda x: lambda y: lambda z: x + y + z)
# print(sum3(2)(4)(6))
# --------------------------

# сортировка
# d = {'b': 15, 'a': 10, 'c': 4}  # kortej
# lst = list(d.items())
# print(lst)
# lst.sort(key=lambda i: i[1]) # sort po pervomu index kazdogo korteja
# print(lst)
# ----------------------

# сортировка

# def func(i):
#     return i[1]
#
#
# d = {'b': 15, 'a': 10, 'c': 4}  # kortej
# lst = list(d.items())
# print(lst)
# lst.sort(key=func)
# print(lst)

# -------------------------------------
# video 24 para
# players = [  # nabor slovarey
#     {'name': 'Антон', 'last name': 'Биоюков', 'rating': 9},
#     {'name': 'Алексей', 'last name': 'Бодня', 'rating': 10},
#     {'name': 'Федор', 'last name': 'Сидоров', 'rating': 4},
#     {'name': 'Михаил', 'last name': 'Семенов', 'rating': 6},
# ]
#
# res = sorted(players, key=lambda item: item['last name'])
# print(res)
#
# res = sorted(players, key=lambda item: item['rating'])
# print(res)
#
# res = sorted(players, key=lambda item: item['rating'], reverse=True)
# print(res)

# --------------
# video 24 para 15 minuta
# a = [(lambda x, y: x + y), (lambda x, y: x - y), (lambda x, y: x * y), (lambda x, y: x / y)]
# b = a[1](15, 5)  # выполняется выражение с индексом 1, т.е. вычитание 15 - 5
# print(b)
# ----------------
#
# a = {'one': lambda x: x - 1, 'two': lambda x: x + 3, 'three': lambda x: x}
# b = [-3, 10, 0, 2]
# for i in b:
#     if i < 0:
#         print(a['two'](i))
#     elif i > 0:
#         print(a['one'](i))
#     else:
#         print(a['three'](i))

# ------------------------
# d = {
#     1: lambda: print('Понедельник'),
#     2: lambda: print('Вторник'),
#     3: lambda: print('Среда'),
#     4: lambda: print('Четверг'),
#     5: lambda: print('Пятница'),
#     6: lambda: print('Суббота'),
#     7: lambda: print('Воскресенье'),
# }
#
# d[4]()

# --------------------------
# проверяется какое число больше:
# print((lambda a, b: a if a > b else b)(15, 13))
# ----------------
# минимальное между элементами:
# print((lambda a, b, c: a if a < b and a < c else b if b < c else c)(9, 8, 5))
# print((lambda a, b, c: min((a, b, c)))(10, -1, 2))

# -----------------
# video 24 para 35 minuta
# map(func, iterable) !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


# function returns a map object(which is an iterator) of the results after applying the given function
# to each item of a given iterable (list, tuple etc.)
# возвращает объект карты (который является итератором) результатов после применения данной функции
# к каждому элементу данной итерации (список, кортеж и т. д.)

# def mult(t):
#     return t * 2
#
#
# lst = [1, 8, 12, -5, -10]  # список
#
# lst2 = list(map(mult, lst))
# lst3 = tuple(map(mult, lst))
#
# print(lst2)
# print(lst3)
#
# print(list(map(lambda t: t * 2, lst)))

# ---

# t = (2.88, -1.75, 100.55)
#
# print(tuple(map(lambda x: int(x), t)))
# print(tuple(map(int, t)))

# ---

# areas = [3.45678, 5.5788666, 7.45474756756, 45.547547, 78.98765, 1.234566]
#
# print(list(map(round, areas, range(1, 3))))
# # print(list(map(int, areas, range(1, 3))))
#
# print(round(3.4567, 2))

# st = ['a', 'b', 'c', 'd', 'e']
# num = [1, 2, 3, 4, 5]
#
# print(list(map(lambda x, y: (x, y), st, num)))  # [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]
# print(dict(map(lambda x, y: (x, y), st, num)))  # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# -------------
# zadacha: naiti poelementno summu chisel dvuh spiskov:
# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
#
# print(list(map(lambda x, y: (x+y), l1, l2)))

# -----------

# filter(func, iterable) - prinimaet funkciu and iteriruemii object, rabotaet kak map() !!!!!!!!!!!!!!!!!!!!!!!!!!!!

# ---
# t = ('abcd', 'abc', 'cdefg', 'def', 'ghi')  # iteriruemii object, tuple
#
# print(tuple(filter(lambda s: len(s) == 3, t)))
# ---

# b = [66, 90, 68, 59, 76, 60, 80, 88, 74, 81, 65]
# res = list(filter(lambda s: s > 75, b))
# print(res)

# zadacha video 24para 01:10 minuts
# : Сгенерировать список из десяти элементов случайным образом.
# Из полученного списка чисел выбрать только те, которые находятся в диапазоне от 10 до 20 (включительно).

# import random
#
# lst = [random.randint(1, 30) for _ in range(10)]
# lst_new = list(filter(lambda x: 9 < x < 21, lst))
# print(lst)
# print('[10; 20] =', lst_new)

m = list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(10))))  # v filter = [1, 3, 5, 7, 9]
print(m)
m1 = [x ** 2 for x in range(10) if x % 2]
print(m1)
