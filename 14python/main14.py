# video 27para, 8 minuta
# 17 minuts
# q = 'Pyt'
# w = 'hon'
# e = q + w
# print(e)
# print(e * 3)
#
# print(e in "I am learn Python") # проверка есть ли слово Python в предложении
# print(e[-1])
# print(e[1:16])
# print(e[::-1])  #Razvorachivaem v protivopoloznuyu storonu = nohtyP
# print(e[5:0:-1])  # = nohty
# print(e[3])
# e = e[:3] + "t" + e[4:]  # zamena bukvi h na t
# print(e)

# -------------------
# zadacha video 27para, 40 minuta

# def changeCharToStr(s, c_old, c_new):
#     s2 = ""
#     i = 0
#     while i < len(s):
#         if s[i] == c_old:
#             s2 += c_new
#         else:
#             s2 += s[i]
#         i += 1
#     return s2
#
#
# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования."
# str2 = changeCharToStr(str1, "N", "P")
# print(str1)
# print(str2)  # Я изучаю Python. Мне нравится Python. Python очень интересный язык программирования.

#  --------------------------------
# Префиксы строк!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# r -префикс
# print('C:\\program\\file\\')  # C:\program\file\
# print(r'C:\program\file' + "\\")  # C:\program\file\
# print(r'C:\program\file\\'[:-1])  # C:\program\file\

# -------
# b - префикс

# print(b'a1b2c3')
# print(b'a1b2c3'[1])
# print(b'\xff\xfe\xfd')
# print(b'\xff\xfe\xfd'[1])

# ---
# f - префикс

# name = "Дмитрий"
# age = 25
# print("Меня зовут ", name, ". Мне ", age, " лет.", sep="")  # sep - убирает пробел - запятую
# print("Меня зовут " + name + ". Мне " + str(age), "лет.")  # конкатенация - + ххх +
#
# print(f"Меня зовут {name}. Мне {age} лет.")  # используется префиксы строк - f

# Вывод:
# Меня зовут Дмитрий. Мне 25 лет.
# Меня зовут Дмитрий. Мне 25 лет.
# Меня зовут Дмитрий. Мне 25 лет.

# ---

# from math import pi

# print(f"Значение числа pi: {round(pi, 2)}")
# print(f"Значение числа pi: {pi:.2f}")
# ---
#
# x = 10
# y = 5
# print(f"{x = }\n{y = }")
# print(f"{x} x {y} / 2 = {x * y / 2}")
# ---

# a = 74
# print(f"{{{{{a}}}}}")

# ---

# fr - префикс

# dir_name = "my_doc"
# file_name = "file.txt"
# print(fr"home\{dir_name}\{file_name}")  # !!!!!!!!!!!!
# print(f"home\\{dir_name}\\{file_name}")
# print(fr"home\{dir_name}\{file_name}")
# print("home\\" + dir_name + "\\" + file_name)

# ---

# video 28 para main 14, 6 minuts

# s = """
# <div>
#     <a href="#">content</a>
# </div>
# """
# s1 = '''
# <div>
#     <a href="#">content</a>
# </div>
# '''
# print(s)
# print(s1)

# ---
# документация:

# def square(n):
#     """Принимает число n, возвращает квадрат числа n"""
#     return n ** 2
#
#
# print(square(5))
# print(square.__doc__)
# print()
# print(len.__doc__)

# ---
# import math as m
#
#
# def cylinder(r, h):
#     """
#     Вычисляет площадь цилиндра.
#
#     Вычисляет площадь цилиндра на основании заданной высоты и радиуса основания
#
#     :param r: положительное число, радиус основания цилиндра
#     :param h: положительное число, высота цилиндра
#     :return: положительное число, площадь цилиндра
#     """
#     return 2 * m.pi * r * (r + h)
#
#
# print(cylinder(2, 4))
# print(cylinder.__doc__)
# ---

# код символов video 28 para main 14, 30 minuts

# print(ord('a'))  # ASCII
# print(ord('#'))  # ASCII
# print(ord('к'))  # юникод русского символа к
#
# # вывести код вводимого символа:
# while True:
#     n = input("->")
#     if n != "-1":
#         print(ord(n))
#     else:
#         break

# ------
# zadacha video 28 para main 14, 38 minuts

# my_str = "Test string for mes"
# arr = [ord(x) for x in my_str]
# print("ASCII коды:", arr)
# # mean = round(sum(arr) / len(arr))
# # arr.insert(0, mean)
# arr = [int(sum(arr) / len(arr))] + arr
# print("Среднее арифметическое:", arr)
# # arr += [x for x in [ord(x) for x in (input("-> "))]]
# arr += [x for x in [ord(x) for x in (input("-> " + " ")[:6])] if x not in arr]
# print(arr)
#
# # по срезу от первого элемента до последнего:
# if arr[-1] in arr[:-1]:
#     print("Количество последних элементов:", arr.count(arr[-1]) - 1)
#
# arr.sort(reverse=True)  # сортировка по убыванию
# print(arr)

# ----
# преобразование из кодов символа в буквы- символы:
# print(chr(84))
# print(chr(101))
# print(chr(1085))

# zadacha
# video 28 para, main14, 01:08 min
# Даны два числа: a = 122, b = 97, где a и b - коды символов. Ваша задача - вывести все символы, ASCII - коды
# которых лежат между a и b включительно, в порядке возрастания их кодов.

# a = [chr(x) for x in range(97, 122 + 1)]
# print(a)
a = 122
b = 97

print(*(chr(x) for x in range(a, b + 1)) if a < b else (chr(x) for x in range(b, a + 1)))

q = [chr(x) for x in range(min(a, b), max(a, b) + 1)]
print(*q)

# --------------
