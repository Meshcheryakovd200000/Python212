# video 19 para   "dict" словари !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# d = {'one': 1, 'two': 2, 'three': 3}
# key = 'two1'
#
# # if key in d:
# #    del d[key]
#
# try:  # пробовать
#     del d[key]
# except KeyError:
#     print("Элемент с ключом", key, "нет в словаре")
# print(d)
#
# -----------------------------------------------
# # Dan slovar s chislovimi znacheniymi.Neobhodimo ih vse peremnojit and vivesti na ecran.
# # {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}

# d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# # print(type(d))
#
# mult = 1
#
# for key in d:
#     mult *= d[key]
#
# print(mult)
# -----------------------------------------------

# Predlojite polzovatelu vvesti nazvaniya 4h ovoshei and sohranite ih v 'dict' s chislovimi indeksami, nachinaya s 1.
# Vivedite soderjimoe slovarya s ukazaniem indexov and elementov. Sprosite polzovatelya, kakoi element on
# hochet iskluchit, and delete ego iz spiska. Vivedite soderjimoe slovarya.

# # d = dict()
# # d[1] = input("-> ")
# # d[2] = input("-> ")
# # d[3] = input("-> ")
# # d[4] = input("-> ")
# d = {key: input("-> ") for key in range(1, 5)}
# print(d)
# dislike = int(input("Исключить: "))
# del d[dislike]
# print(d)

# ------------------------------------------------------
# v dict mojno poschitat dlinu
# d = {'one': 1, 'two': 2, 'three': 3}
# print(len(d))
# -----------------------------------------------------

# video 19 para 29 minuta
# Задача:

# goods = {  # Товары:
#     "1": ["Core-i3-4330", 9, 4500],
#     "2": ["Core i5-4670K", 3, 8500],
#     "3": ["AMD FX-6300", 6, 3700],
#     "4": ["Pentium G3220", 8, 2100],
#     "5": ["Core i5-3450", 5, 6400]
# }
#
# for key in goods:
#     print(key, ")", goods[key][0], " - ", goods[key][1], "шт. по ", goods[key][2], " руб.",
#           sep="")  # sep="" - chtobi lishnih probelov nebilo
#
# while True:
#     n = input("Номер товара: ")
#     if n != "0":
#         m = int(input("Количество товара: "))
#         goods[n][1] = m
#     else:
#         break
#
# for key in goods:
#     print(key, ")", goods[key][0], " - ", goods[key][1], "шт. по ", goods[key][2], " руб.",
#           sep="")  # sep="" - chtobi lishnih probelov nebilo


# Методы словарей - metodi dicts !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# get(), keys(), items(), values(), clear(), copy(), pop(), setdefault(), popitem(), update(), zip()-function,

# ----------------
# d = {'one': 1, 'two': 2, 'three': 3}
# print(d["two"])
# value = d.get("two1", "Ключа нет")  # poluchaem element iz dict po zadannomu key, 2oi parametr vozvrashaet znachenie
# # po umolchaniu if key net
# print(value)
# # ----------------
# d = {'one': 1, 'two': 2, 'three': 3}
# print(d.keys())  # список ключей словаря
# print(d.items())  # список ключей и значений словаря в виде кортежа
# print(d.values())  # список значений словаря
#
# for key, value in d.items():  # raspakovka korteja, v kajduu peremennuu sohranili svoe znachenie
#     print(key, "=>", value)
#
# d.clear()  # ochistit slovar
# print(d)
# ----------------
# d = {'one': 1, 'two': 2, 'three': 3}
# d2 = d.copy()  # copiya dict
# print("D1 =", d)
# print("D2 =", d2)
#
# d["four"] = 4
# d2["five"] = 5
# print("D1 =", d)
# print("D2 =", d2)

# d = {'one': 1, 'two': 2, 'three': 3}
#
# # item = d.pop('two')  # udalyaet element po key, vozvrashaet udalyaemoe znachenie (ne key)
# # item = d.pop('two', "Ключа нет")
# # ------------
# # item = d.setdefault("four", 4)  # dobavlyaet key and znachenie v dict po umolchaniu, if key net (value pomenyat ne mojem)
# # ------------
# # item = d.popitem()  # delete poslednuu (proizvolnuu) paru key and value, vozvrashaet udalyaemoe value v vide korteja
# # print(item)
# # print(d)
#
# # d.update({'four': 4, 'five': 5})  # esli key est to menyaet znachenie, if key net to dobavlyaetsya key and value
# d.update([('four', 4), ('three', 5)])  # dobavlyaem informaciu v vide korteja
# print(d)

# video 20 para

# -----------------------------
# Obedinenie 2uh dict

# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}
# # z = x.copy()
# # z.update(y)
# # z = x | y  # obedinenie slovarei s sohraneniem v new dict
# z = {i: d[i] for d in [x, y] for i in d}
# print(z)

# -----------------------------

# Дан словарь {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}.
# Создать новый словарь, который будет содержать только имя и зарплату сотрудника,
# а затем удалить эти значения из исходного словаря.

# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# # new_d = dict()
# # new_d['name'] = d.pop('name')
# # new_d['salary'] = d.pop('salary')
# # new_d.update({'name': d.pop('name'), 'salary': d.pop('salary')})
# new_d = {'name': d.pop('name'), 'salary': d.pop('salary')}
# print(d)
# print(new_d)
# -----------------------------

# Dan dict {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}. Pereimenovat
# key 'city' v 'location'.

# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# d['location'] = d.pop('city')
# print(d)
# --------------------------------

# a = {
#     'first': {
#         1: 'one',
#         2: 'two',
#         3: 'three'
#     },
#     'second':{
#         4: 'four',
#         5: 'five'
#     },
# }
# print(a)
# for x in a:
#     print(x)
#     for y in a[x]:
#         print("\t", y, ": ", a[x][y], sep="")

# --------------------------------
# video 20 para, 31 minuta

# sales = {
#     "John": {"N": 3056, "S": 8463, "E": 8441, "W": 2694},
#     "Tom": {"N": 4832, "S": 6786, "E": 4737, "W": 3612},
#     "Anne": {"N": 5239, "S": 4802, "E": 5820, "W": 1859},
#     "Fiona": {"N": 3904, "S": 3645, "E": 8821, "W": 2451},
# }
#
# for x in sales:
#     print(x)
#     for y in sales[x]:
#         print("\t", y, ": ", sales[x][y], sep="")
#
# person = input("Имя: ")
# region = input("Регион: ")
# print(sales[person][region])
# new_data = int(input("Новое значение: "))
# sales[person][region] = new_data
# print(sales[person])

# ----------------------

# menyaem mestami key and value:
# d = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
# new_d = {k: v for k, v in d.items()}
# print(new_d)
# new_d = {v: k for k, v in d.items()}
# print(new_d)

# ----------------------

# Iz ishodnogo dict {'один': 1, 'два': 2, 'три': 3, 'четыре': 4} vivedite tolko dva pervih key and value

# d = {'три': 3, 'один': 1, 'два': 2, 'четыре': 4}
# new_d = {k: v for k, v in d.items() if v <= 2}  # if v == 1 or v == 2
# print(new_d)

# --------------------

# iz stroki v slovar (dict)

# s = "Hello"
# d = {i: i*3 for i in s}
# print(d)

# ---------------------
# Ввод значений одно или несколько:
lt = [1, 2, 3, 4]
# value = input("->")
d = {i: input("->") for i in lt}
print(d)

# ---------------------
# preobrazovanie iz dict v list
# d = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
# # value = list(d)
# # value = list(d.values())
# value = list(d.items())
# print(value)
# --------------------
# video 20 para, 58 minut

# Preobrazovat list ["one", 1, 2, 3, "two", 10, 20, "three", 15, 36, 60, "four", -20] v slovar (dict), tak,
# chtobi strokovie znacheniya bili key, and chislovie - znacheniyami.

# a = ["one", 1, 2, 3, "two", 10, 20, "three", 15, 36, 60, "four", -20]
#
# d = dict()
# s = None
#
# for i in a:
#     if type(i) == str:
#         d[i] = []
#         s = i  # s = 'two'
#     else:
#         d[s].append(i)  # d['two'].append(10)
# print(d)

# ------------------------

# zip() function !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# iz neskolkih spiskov preobrazuet v slovar!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# d = dict(zip([1, 2, 3], ['one', 'two', 'three']))
# print(d)
#
# # generator dicts (генератор словарей):
#
# a = [1, 2, 3]
# b = ['one', 'two', 'three']
# f = {k: v for k, v in zip(a, b)}
# print(f)
# f2 = {k: v for k, v in zip(b, a)}
# print(f2)

# d = list(zip([1, 2, 3], ['one', 'two', 'three']))
# print(d)
#
# d = dict(zip('one', 'two'))
# print(d)

# a = [1, 2, 3]
# print(list(zip(a)))
#
# print(list(zip(range(5), range(95, 100))))

# a = [1, 2, 3]
# b = {'one', 'two', 'three'}
# c = (4.0, 5.4, 6.7)
# # print(tuple(zip(a, b, c)))
# print(list(zip(a, b, c)))
