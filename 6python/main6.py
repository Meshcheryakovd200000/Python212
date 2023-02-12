# video Python, 15.12.2022, 10 пара

# etot variant esli vtoroi spisok bolshe
# a = [1, 2, 3, 4, 2, 55, 99]
# b = [11, 22, 33, 14]
# c = []
# print("a", a)
# print("b", b)
#
# if len(b) > len(a):
#     for i in range(len(a)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)):  # range(3,5)
#         c.append(b[i])
# # vtoroi variant esli pervii spisok bolshe
# else:
#     for i in range(len(b)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(b), len(a)):  # range(3,5)
#         c.append(a[i])
# print(c)
# -----------------------

# a = [1, 2, 3, 4, 2, 55, 99]
# a.remove(2)  # udalyaet iz spiska ukazannii element po znacheniu. Esli elementov neskolko, to udalitsya tolko pervii.
# print(a)
# last = a.pop()  #  udalyaet poslednii element iz spiska i vozvraschaet udalyaemoe znachenie
# print(last)
# print(a)
# last = a.pop(-2)  #  udalyaet element po index
# print(last)
# print(a)
# a.clear()  # udalyaet iz spiska vse elementi
# print(a)

# Example: Dan spisok iz chisel and index elementa v spiske k. Udalite iz spiska element s indeksom k, sdvinuv vlevo vse
# elementi, stoyaschie pravee elementa s indecsom k.

# a = [int(input("Введите елементы списка: ")) for i in range(int(input("Введите количество элементов списка: ")))]
# k = int(input("Введите удаляемый индекс: "))
# print(a)
# a.pop(k)
# print(a)

# ----------
# a = []
# [a.append(input("->")) for i in range(int(input("n = ")))]
# print(a)
# while True:
#     if len(a) == 0:
#         break
#     k = int(input("Введите индекс: \n k = "))
#     a.pop(k)
#     print(a)

# a = [9, 5, 9, 7, 6, 9, 4, 9, 0, 9]
# print(a)
# num = a.count(9)  # kolichestvo zadannih znachenii v spiske
# print("Количество девяток: ", num)
# ind = a.index(9, 6, -1)  # 9- eto znachenie, poisk ot 6 do -1 index. Esli znachenie ne naideno, to iskluchenie
# # "# ValueError"
# print("Поиск цифры 9 в интервале от 6 ого индекса до -2 индекса, в этом списке цифра 9 стоит на индексе: ", ind)
#
# # video, Python, 15.12.2022, 11 пара !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#
# ch = 7
# if ch in a:
#     ind = a.index(ch)  # esli ch=7 est v spiske to vivodim
#     print(ind)

# a = [5, 9, 7]
# b = a
# print("a =", a)
# print("b =", b)
# b.append(120)
# print("a =", a)
# print("b =", b)
# print(id(a))
# print(id(b))

# a = [5, 9, 7]
# b = a.copy()  #  sozdaet copiyu spiska
# print("a =", a)
# print("b =", b)
# b.append(120)
# print("a =", a)
# print("b =", b)
# print(id(a))
# print(id(b))

# a = [5, 9, 7, 6, 9, 4, 9, 0, 9]
# a.reverse()  # peremeshaet elementy spiska v obratnom poryadke
# print(a)
# # a.sort()  # sortiruet elementy spiska po vozrastaniyu
# # print(a)
# a.sort(reverse=True) # sortirovka elementov spiska po ubivaniyu
# print(a)
#
# b = sorted(a, reverse=True)
# print("b =", b)
# print("a =", a)

# s = ['Виталий', 'Сергей', 'Александр', 'Анна']
# print(s)
# s.sort(reverse=False)
# print(s)
# s.sort(key=len)  # sortirovka po kolichestvu elementov
# print(s)
# s.sort(key=len, reverse=True)
# print(s)

# video Python, 15.12.2022, 11 пара 28 minutes
# dir(list) - vvodim v Python console

# Generacia sluchainich dannih!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# 1 sposob podklucheniya modulya random:

# import random
#
# print(random.random())
# print(random.randint(0, 9))  # ot 0 do 9 (9 - vkluchaetsya)
# print(random.randrange(0, 9))  # ot 0 do 9 (9 - ne vkluchaetsya)
#
# print(random.randrange(0, 9, 2))

# 2 sposob podklucheniya modulya random:

# from random import randint, randrange
#
# print(randint(1, 9))
# print(randrange(1, 9))
#
# # 3 sposob importa moduley
#
# from random import *  # -import vsex moduley
#
# print(randint(1, 9))
# print(randrange(1, 9))
#


# # 4 variant importa moduley
#
# a = 5

# import random as r

# print(r.randint(1, 9))
# print(r.randrange(9))
# print(r.uniform(10.5, 25.5))

# city = ['Москва', 'Новосибирск', 'Воронеж', 'Сочи', 'Екатеринбург']
# print(r.choice(city))
# print(r.choices(city, k=3))
# r.shuffle(city)
# print(city)

# city = [3, 5, 9, 8, 7, 6]
# print(r.choice(city))
# print(r.choices(city, k=3))
# r.shuffle(city)
# print(city)

# !!!!!!!!!!! 3 primera kak zapisat randomizaciyu: !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# mas = [i for i in range(10)]
# mas = [input("->") for i in range(10)]
# mas = [r.randint(50, 100) for i in range(20)]
# print(mas)

# lst = [4, 6, 8, 9, 1]
# print(min(lst))
# print(max(lst))
# print(sum(lst))


# 11 para video 01:06

# Zapolnit spisok iz 10 elementov sluchainimi chislami. Naiti max. element spiska and peremestit ego v nachalo spiska

# from random import randint, randrange
#
# mas = [randint(1, 20) for i in range(10)]
# print(mas)
# maxi = max(mas)
# print(maxi)
# mas.remove(maxi)
# mas.insert(0, maxi)
# print(mas)

# video 12 para

# Zapolniti spisok iz 10 elementov sluvhainimi chislami kak polozitelnimi tak and otricatelnimi. Izmenit etot spisok
# takim obrazom, chtobi vse otricatelnie elementi okazalis v konce.

# from random import randint
#
# mas = [randint(-20, 20) for i in range(10)]
# print(mas)
# mas.sort(reverse=True)
# print(mas)

# Zapolnit spisok iz 10 elementov sluchainimi chislami. Udalit vse elementi, raspolozennie pered minimalnim
# elementom spiska.

# from random import randint
#
# spi = [randint(0, 100) for i in range(10)]
# print(spi)
# spi_min = min(spi)
# print("Min: ", spi_min)
# spi_index = spi.index(spi_min)
# print("Index min: ", spi_index)
# del spi[:spi_index]   #  or  spi2 = spi[spi_index:]
# print(spi)

# video 12 para, 13 minut

# x = list('1a2b3c4d')
# print(x)
# print('a' not in x)
# print('e' not in x)
#
# lst = []
# if len(lst) == 0:
#     print("Список пустой")
#
# if not lst:
#     print("Список пустой")

# ----------------------------------------------------------------------------------

# import random as r
#
# n1 = int(input("Введите размер первого списка: "))
# n2 = int(input("Введите размер второго списка: "))
# a = [r.randint(0, 10) for _ in range(n1)]
# b = [r.randint(0, 10) for _ in range(n2)]
# print("Первый список: ", a)
# print("Второй список: ", b)
# c = a + b
# print("Третий список", c)
#
# c = []
# for i in range(len(a)):
#     if a[i] not in c:
#         c.append(a[i])
# for i in range(len(b)):
#     if b[i] not in c:
#         c.append(b[i])
# print("Элементы обоих списков без повторений: ", c)
#
# c = []
# for i in a:
#     if i in b and i not in c:
#         c.append(i)
# print("Элементы общие для двух списков", c)
#
# c = [min(a), min(b), max(a), max(b)]
# print("min and max значение каждого из списков: ", c)

# --------------------------------------------------------------------

# 1 s range i s indexami:
m = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
print(m)
# print(len(m))
# print(m[1][2])
# for row in range(len(m)):  # row - eto stroka
#     # print(m[row])
#     for col in range(len(m[row])): # dostup k elementam kazdoi stroki
#         print(m[row][col], end="\t")
#     print()
# print()

# 2

# for row in m:
#     for x in row:
#         print(x, end="\t")
#     print()
#
# # Vozvesti kazdii element v kvadrat
#
# for row in m:
#     for x in row:
#         print(x**2, end="\t\t")
#     print()

# w, h = 10, 10
# matrix = [[x*y for x in range(1, w)] for y in range(1, h)]
# # matrix = []
# # for y in range(h):
# #     new_row = []
# #     for x in range(w):
# #         new_row.append(0)
# #     matrix.append(new_row)
# print(matrix)
# for h in matrix:
#     for w in h:
#         print(w, end="\t\t")
#     print()
# print()

# --------------------------------------------------
for x, y in [[1, 2],[3, 4], [5, 6], [7, 8]]:
    print(x, "+", y, "=", x + y)

# video 12 para konec