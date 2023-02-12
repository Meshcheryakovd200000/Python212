# print('apple' == 'Apple')
# print('apple' > 'Apple')
# print(ord('a'))  # 97
# print(ord('A'))  # 65

# длина пароля 'строки'
# from random import randint
#
# SHORTEST = 8
# LONGEST = 16
# MIN_ASCII = 33
# MAX_ASCII = 126
#
#
# def random_password():
#     random_length = randint(SHORTEST, LONGEST)
#     res = ''
#
#     for i in range(random_length):
#         random_char = chr(randint(MIN_ASCII, MAX_ASCII))
#         res += random_char
#     return res
#
#
# print("Ваш случайный пароль:", random_password())

# print(dir(str))
# ---
# s = "hello, WORLD! I am learning Python."
# print(s.capitalize())  # приводит первую букву в верхний регистр, остальные в нижний
# print(s.lower())  # перобразует все символы в нижний регистр
# print(s.upper())  # перобразует все символы в верхний регистр
# print(s.swapcase())  # меняет регистр на противоположный
#
# print(s.count('h', 1))  # ищем с 1ого символа букву h (подсчитывает кол-во вхождений подстроки в строку)
# print(s.lower().count('o', 0, -5))  # сначало в нижний регистр преобразуем, потом считаем
#
# print(s.find("Python"))  # возвращает первый индекс который соответствует заданной подстроке.
# # Если совпадений нет то вернется значение -1
#
# print(s.find("Python", -3))
#
# print(s.index("Python"))  # возвращает первый индекс который соответствует заданной подстроке.
# # Если соврадений нет то возвращается ошибка ValueError

# ------------------------
# zadacha video 57 minuta

# s = 'один два'
# ind = s.find(' ')
# s = s[ind + 1:] + ' ' + s[:ind]
# print(ind)

# zadacha video 01:07

# s = 'ab12c59p7dq'
# digits = []
# for symbol in s:
#     if '1234567890'.find(symbol) != -1:
#         digits.append(int(symbol))
# print(digits)


# s = "hello, WORLD! I am learning Python."
# print(s.rfind("l"))
# print(s.rindex("l"))
# print(s.find("l", 4))

# zadacha

# a = "Nearly all web services collect this basic information from users in their server logs. " \
#     "However, Python Tutor does not collect any personally identifiable information from its users."
#
# n = 'f'
#
# if a.count(n) == 1:
#     print(a.find(n))
# elif a.count(n) >= 2:
#     print(a.find(n), a.rfind(n))
# --------------------------

# zadacha
# s = "I am learning Python, hello, WORLD"
# ind1 = s.find('h')
# print(ind1)
# ind2 = s.rfind('h')
# print(ind2)
# res = s[0:ind1] + s[ind2 + 1:]
# print(res)
# ----------------

# s = "hello, WORLD! I am learning Python."
# print(s.startswith("hello")) # строка начинается с текущего элемента (с чего начинается строка)
# print(s.endswith("Python.")) # чем заканчивается строка
# # возвращает True или False

# --------------

# print('abc123'.isalnum())  # строка состоит из букв и цифр
# print('abc?123'.isalnum())
# print(''.isalnum())
#
# print('abc'.isalpha())  # проверка что строка состоит только из букв (любой регистр)
# print('abc123'.isalpha())
#
# print('abc123'.isdigit())
# print('123'.isdigit())  # строка состоит только из цифр

# print('py'.center(10, "-"))
# print('py'.center(7, "="))
# ---
# print("    py".lstrip())  # удаление пробельных символов слева
# print("    py".rstrip())  # удаление пробельных символов справа
# print("    py     ".rstrip())  # удаление пробельных символов справа и слева одновременно
#
# print('https://www.python.org'.lstrip('/:pths'))  # удаляет слева символы
# print('py.$$$;'.rstrip(';$.'))  # удаляет слева символы
#
# print('https://www.python.org'.strip('/:pths.orgw'))  # удаляет слева и справа
# print('https://www.python.org'.lstrip('/:pths').rstrip('.orgw'))  # удаляет слева и справа
# ---

# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования."
# # print(str1.replace("N", "P"))
# print(str1.replace("Nython", "Python", 2))  # колличество заменяемых элементов

# s = "-"
# seq = ('a', 'b', 'c')
# print(s.join(seq))
#
# print("..".join(['1', '99']))
# print("..".join(['1', '2']))
#
# print(":".join("Hello"))  # объединяет итерируемую последовательность в  строку через символ разделитель

# print("Строка разделенная пробелами".split())
# print('www.python.org.ru'.split(".", 2))
# print('1,2,3'.split(","))
# print('www.python.org.ru'.rsplit(".", 2))

# a = input("->").split()
# print(a)
# a = list(map(int, a))
# print(a)

# zadacha video 02:30 minuts

# s = "В строке заменить пробелы звездочками"
# s = s.split()
# print(s)
# s = "*".join(s)
# print(s)
# ------------------

# zadacha
# s = "Никонов Валерий Анатольевич"

# s = input('FIO: ').split()
# print(s)
# print(f'{s[0]} {s[1][0]}. {s[2][0]}.')

# Регулярные выражения - это язык поиска

import re

# print(dir(re))

# s = "Я ищу совпадения в 2023 году. И я их найду в 2 счёта."
# reg = r'\.'
# print(re.findall(reg, s))  # возвращает список содержащий все совпадения с заданным шаблоном
#
# print(re.search(reg, s))  # возвращает данные по соответствию первого совпадения с шаблоном
# # print(re.search(reg, s).span())
# # print(re.search(reg, s).start())
# # print(re.search(reg, s).end())
# # print(re.search(reg, s).group())
#
# print(re.match(reg, s))  # совпадения шаблона от начала строки (поиск по заданному шаблону в начале строки)

# print(re.split(reg, s, 1)) # разбиваем строку на список подстрок

# поиск и замена:

# print(re.sub(reg, "!", s, 1))  # поиск и замена
# ----------

s = "Я ищу совпадения в 2023 году. И я их найду в 2 счёта. 9812"
reg = r'[2023]'

print(re.findall(reg, s))

# в папке 17 есть картинка название = Комбинации
reg = r'2[0-9][0-9][0-9]'
print(re.findall(reg, s))
