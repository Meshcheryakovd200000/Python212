# video 17 para

# t = (1, 2, 3)
# # del t
# # print(t)
#
# print(t)
# t = list(t)  # preobrazuem v spisok
# print(t)
# t.append(4)
# print(t)
# t = tuple(t)  # preobrazuem v kortez dobaviv element v spisok
# print(t)

# Tuple so vlojennimi elementami
# countries = (
#     ("Германия", 80.2, (("Берлин", 3.326), ("Гамбург", 1.718))),
#     ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6)))
# )
#
# # raspakovka tuple
# for country in countries:
#     countryName, countryPopulation, cities = country
#     print("\nСтрана:", countryName, ", население =", countryPopulation)
#     for city in cities:
#         cityName, cityPopulation = city
#         print("\tГород:", cityName, ", население =", cityPopulation)


# Множество(mnojestvo) - "set" !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1
# - неупорядоченный коллекционный тип данных который хранит уникальный тип данных
# (neuporyadochennii kollekcionnii tip dannih kotorii hranit unikalnii tip dannih)
# set nujen for bistrogo nahojdeniya unicalnogo elementa

# s = {"banana", "apple", "orange", "apple"}
# print(type(s))
# print(len(s))
# print(s)


# b = 'Hello', 'Hi'
# a = set(b)
# print(type(a))
# print(a)


# s = {x * x for x in range(10)}
# print(s)

# numbers = [1, 2, 2, 2, 3, 3, 4, 4, 5, 6]
# # num = {i for i in numbers if i % 2 == 0}  # vivodim chetnie chisla
# num = list(set(numbers))
# print(type(num))
# print(num)


# video 17para 40 minut

# На входе функция to_set()  получает строку или список чисел. Преобразуйте их в множество.
# На выходе должно получиться множество и количество элементов в нем.

# def to_set(s):
#     print(s)
#     st = set(s)
#     return st, len(st)
#
#
# print(to_set('я обычная строка'))
# print(to_set([4, 5, 4, 6, 2, 9, 11, 3, 4, 2]))

# t = {'red', 'green', 'blue'}
# print('green' not in t)

# pr = {2, 5, 3, 7, 11}
# for i in pr:  # in pr
#     print(i, end=" ")

# video 17 para 50 minut

# s = ['ab_1', 'ac_2', 'bc_1', 'bc_2']
# a = {i for i in s if 'a' not in i}  # if bukva 'a' net v elemente to element vivoditsya
# # a = {'A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in
# #      s}  # kajduyu pervuyu bukvu elementa pereveli v verhnii registr
# a = {'A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in s if i[1] == 'c'}
# print(a)


# a = set()
# a = {0, 1, 2, 3}
# a.add(4)  # dobavlenie elementa
# print(a)
# if 1 in a:
#     a.remove(1)  # delete elementa
# print(a)
# a.discard(5)  # delete elementa bez generacii isklucheniya
# print(a)
# a.pop()  # delete pervogo elementa, generaciya isklucheniya budet pri popitke delete iz pustogo mnojestva
# print(a)
# a.clear()  # ochistka mnojestva
# print(a)

# смотри "Операции с множествамиJPG" в директории D:\Python212\Python\9python

# a = {0, 1, 2, 3, 4}
# b = {3, 2, 1}
# c = a.union(b)
# c = a | b
# a |= b
# c = a & b
# a &= b
# c = b - a
# c = a - b
# a -= b
# c = a ^ b  # cirkuflex
# a ^= b
# c = a <= b
# print(a)
# print(c)

# video 18 para

# ----------------------- video 18 para 6 minuta

# Dan nabor mnojestv:{1, 2}, {3}, {4, 5}, {3, 2, 6}, {6}, {7, 8}, {9,8}
# Naiti kolichestvo unikalnix elementov vo vseh mnojestvah.
# Naiti min and max element sredi nih.

# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}
#
# # s = s1 | s2 | s3 | s4 | s5 | s6 | s7
# s = s1.union(s2, s3, s4, s5, s6, s7)
# print(s)
# print(len(s))
# print("Max =", max(s))
# print("Min =", min(s))

# --------------------------

# Naiti obshie bukvi v raznih strokah

# s1 = "Hello"
# s2 = "How are you"
# s = set(s1) & set(s2)
# # print(s)
# for i in s:
#     print(i, end=" ")

# ----------------------------

# Marina, Jenya, Sveta zanimayutsya risovaniem, and Kostya, Jenya, Iliya - dopolnitelno poseschyaut uroki music.
# Opredelite, skolko chelovek zanimautsya tolko odnim vidom iskusstva and vivedite spisok ih name.
# uchenik, zanimauschiisya v oboih krujkah, reshil brosit zanyatiya risovaniem.
# Proizvesti sootvetstvuuschie izmeneniya

# drawing = {"Марина", "Женя", "Света"}
# music = {"Костя", "Женя", "Илья"}
#
# only_one_hobby = drawing ^ music
# print("Только одно хобби:", only_one_hobby)
#
# both_hobbies = drawing & music
# print("Два хобби:", both_hobbies)
#
# drawing = drawing - both_hobbies
# print("Рисование:", drawing)

# ---------------------------

# frozenset - neizmenyaemii tip dannih  -  video 29 minuta !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# s = frozenset({1, 2, 3, 4, 5})
# print(s)
# print(type(s))



# Словарь (dict) - izmenyaemii tip dannih !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!




# video 18 para 33 minuta

# s = [1, 2]  # spisok
# d = {'one': 1, 'two': 2, 'ten': 10}  # dict - словарь
# print(s[0], s[1])
# print(d['one'], d['two'])
# print(d)

# pustoi slovar:
# -------------------------
# pervii slovar:
# d = {}
# print(d)
# print(type(d))
# # d = None
# d["one"] = "один"
# d["two"] = "два"
# print(d)

# vtoroi slovar:

# d1 = dict()
# print(d1)
# -------------------------
# zapolnennii dict:
# pervii dict:
# d = {"one": "один", "two": "два"}
# print(d)
#
# # vtoroi dict:
# d1 = dict(one="один", two="два")
# print(d1)

# preobrazuem spisok:
# users = [  # list -список
#     ['igor@gmail.com', 'Igor'],
#     ['irina@gmail.com', 'Irina'],
#     ['anna@gmail.com', 'Anna'],
# ]
#
# print(users)
# d_users = dict(users)
# print(d_users)
# print()

user = (  # tuple - кортеж
    ('igor@gmail.com', 'Igor'),
    ('irina@gmail.com', 'Irina'),
    ('anna@gmail.com', 'Anna'),
)

print(user)
d_user = dict(user)
print(d_user)

# print('irina@gmail.com' in d_user)

for key in d_user:
    print(key, "->", d_user[key])
