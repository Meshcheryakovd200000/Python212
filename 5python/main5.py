# name_new = "Dima"  # создание переменной
#  age = 20
#  print("Hello,", name_new)
# print(type(age))

# a = b = c = 1
# print(a, b, c)
#
# a, b, c = "Hello", 5, False
# print(a, b, c)
#
# PI = 3.14
# print(PI)
#
# PI = 2
# print(PI)

# a = "Hello"
# print(a)
# print(type(a))
# a = 5
# print(type(a))

# name = "Olga"
# age = 21
# print("Меня зовут " + name + ". Мне " + str(age))
#
# a = 1
# b = 2
# print("a:", a)
# print("b:", b)
# # a, b = b, a
# c = a
# a = b
# b = c
# print("a:", a)
# print("b:", b)

# print("строка строка символов строка символов строка символов строка символов строка символов строка \
#                 строка символов строка символов строка символов строка символов строка символов символов"
#       " строка "
#       "символов")
# print("строка символов")

# print("Документ \"file.py\" \t\t\t\t\t\t\t\tнаходится по заданному пути \nD:\\Python\\file.py")

# s1 = "Hello"
# s2 = "Python"
# s3 = s1 + ", " + s2 + "!\t\t"
# print(s3)
# print(s3 * 3)

# print(6+2)
# print(6-2)
# print(6*2)
# print(6/5) # 3.0
# print(6//5) # 3
# print(6**2)
# print(7%2)
#
# print(5+7+3)
# print(5*7*3)
# print((5+7+3)/3)

# a, b, c = 5, 7, 3
# summa = a + b + c
# proizv = a*b*c
# sredn = summa / 3
# print("Сумма:", summa)
# print("Произведение: ", proizv)
# print("Среднее арифметическое: ", sredn)

# num = 10
# num += 5 # num = num + 5
# print(num) # 15
#
# num -=3 # num = num -3
# print(num) # 12
#
# num *= 4 # num = num *4
# print(num) # 48

# num = 4321
# a = num % 10
# print(a)
# num = num // 10
# # print(num)
# b = num % 10
# print(b)
# num = num // 10
# # print(num)
# c = num % 10
# print(c)
# num = num // 10
# # print(num)
# d = num % 10
# print(d)
# print(a * 1000 + b * 100 + c * 10 + d)

# num = 4321
# res = num % 10 * 1000
# num //= 10
# res += num % 10 * 100
# num //= 10
# res += num % 10 * 10
# num //= 10
# res += num % 10
# print(res)


# Функции явного преобразования типов
# int()
# str()
# float()
# bool()


# print(6/2)

# num1 = "2.5"
# num2 = 3
# res = float(num1) + num2
# print(res)

# a = 1
# b = 2
# print("a:", a, "\nb:", b)

# name = "Виктор"
# age = 28
# print("Меня зовут", name, ". Мне", age, "лет.")
# print("Меня зовут " + name + ". Мне " + str(age) + " лет.")
# print("Меня зовут", name, ". Мне", age, "лет.", sep="__", end="")
# print("Я учу Python.")

# name = input("Введите имя: ")
# print("Hello", name)

# num = int(input("Введите число: "))
# # print(type(num))
# power = int(input("Введите степень: "))
# # num = int(num)
# # power = int(power)
# res = num ** power
# print("Число", num, "в степени", power, "равно:", res)

# num1 = int(input("Введите любое число: "))
# num2 = int(input("Введите любое число: "))
# num3 = int(input("Введите любое число: "))
# num4 = int(input("Введите любое число: "))
# summ = num1 + num2
# sum2 = num3 + num4
# itog = summ / sum2
# print(round(itog, 2))
#
# print("Ответ:", round((num1 + num2)/(num3 + num4), 2))

# b1 = True
# b2 = False
# print(b1 + 5)  # 1+ 5 = 6
# print(b2 + 5)  # 0+ 5 = 5

# print(bool("python"))
# print(bool("")) # False
# print(bool(" "))
# print(bool("5"))
# print(bool("0")) # False
# print(bool(False)) # False
# print(bool(None)) # False
#
# test = None
# print(test)
# test = 5
# print(test)
#
#
# print(7 == 7)
# print(2+5 != 7)
# print("Привет" > "Привет")

# print(2<4<9) # True  && True => True
# print(2 * 5 > 7 >= 4 + 3) # True && True  => True
# print(3*3 <= 7 >=2) # False && True  =>  False

# a = 10
# b = 5
# c = a == b
#
# print(a, b, c)


# print(5 - 3 == 2 and 1 + 3 == 4) # True (True and True)
# print(5 - 3 == 2 and 1 + 3 < 4) # True (True and False)
#
# print(5 - 3 == 2 or 1 + 3 == 4) # True (True or True)
# print(5 - 3 == 2 or 1 + 3 < 4) # True (True or False)

# print(not 9-5)
# print(not 7-7)

# cnt = 15
# if cnt < 10:
#     cnt += 1
#     print(cnt)

# age = int(input("Введите свой возраст: "))
# if age >= 18:
#     print("Доступ на сайт разрешен")
# else:
#     print("Доступ запрещен")

# a = 35
# b = 35
# if a > b:
#     print("a > b")
# elif a < b:
#     print("b > a")
# else:
#     print("a == b")

# d = input("Введите первую сторону: ")
# e = int(input("Введите вторую сторону: "))
# f = int(input("Введите третью сторону: "))
# if d == e == f:
#     print("Треугольник равносторонний")
# elif d == e or e == f or f == d:
#     print("Треугольник равнобедренный")
# else:
#     print("Треугольник разносторонний")

# day = int(input("Введите день недели (цифрой): "))
# if 1 <= day <= 5:   # if (day >= 1) and (day <= 5): -
#     print("Рабочий день - ", end="")
#     if day == 1:
#         print("понедельник")
#     if day == 2:
#         print("вторник")
#     if day == 3:
#         print("среда")
#     if day == 4:
#         print("четверг")
#     if day == 5:
#         print("пятница")
#
# elif day == 6 or day == 7:
#     print("Выходной день - ", end="")
#     if day == 6:
#         print("суббота")
#     if day == 7:
#         print("воскресенье")
# else:
#     print("Такого дня недели не существует")

# month = int(input("Введите номер месяца: "))
# if 1 <= month <= 2 or month ==12:
#     print("Зима")
# elif 3 <= month <= 5:
#     print("Весна")
# elif 6 <= month <= 8:
#     print("Лето")
# elif 9 <= month <= 11:
#     print("Осень")
# else:
#     print("Нет такого месяца")

# month = int(input("Введите номер месяца: "))
# if 1 <= month <= 12:
#     print("Время года: ", end="")
#     if month == 1 or month == 2 or month == 12:
#         print("Зима")
#     if 3 <= month <= 5:
#         print("Весна")
#     if 6 <= month <= 8:
#         print("Лето")
#     if 9 <= month <= 11:
#         print("Осень")
# else:
#     print("Нет такого месяца")

# n = int(input("Введите колличество ворон: "))
# if 0 <= n <= 9:
#     print("На ветке", n, end=" ")
#     if n == 1:
#         print("ворона")
#     if 2 <= n <= 4:
#         print("вороны")
#     else:               # if 5 <= n <= 9 or n == 0:
#         print("ворон")
# else:
#     print("Ошибка ввода данных")

# a, b = 10, 5
# minim = "a == b" if a == b else "a > b" if a > b else "b > a"
# print(minim)

# a, b = 10, 0
# c = a / b if b != 0 else "На ноль делить нельзя"
# print(c)

# Исключения  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# a = 0
# b = "2a"
# print(a + int(b))

# a = 5
# b = 0
# print(a / b)

# n = int(input("Введите целое число: "))
# print(n * 2)

# try:   # попробуй
#     n = int(input("Введите целое число: "))
#     print(n * 2)
# except ValueError:    # кроме
#     print("Что-то пошло не так")


# try:   # попробуй
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except ValueError:    # кроме (исключение) пояснение
#     print("Что-то пошло не так")
# except ZeroDivisionError:
#     print("Нельзя делить на ноль")

# try:   # попробуй
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except (ValueError, ZeroDivisionError):    # кроме (исключение) пояснение
#     print("Нельзя вводить строки или делить на ноль")
# else:
#     print("Все нормально. Вы ввели", n, "и", m)  # когда в блоке try не возникло исключение
# finally:
#     print("Конец программы") # выполняется в любом случае

#
# q = input("Введите первое число: ")
# w = input("Введите второе число: ")
#
# try:
#     q = int(q)
#     w = int(w)
# except ValueError:
#     q = str(q)
# finally:
#     print(q + w)

# Цикл while

# while условие:
#       тело цикла

# i = 0
# while i < 5:
#     print("i =", i)
#     i += 1          # i = i + 1

# i =10
# while i > 0:
#     print("i =", i)
#     i -= 1

# i = 1
# while i < 21:
#     if i % 2 == 0:
#         print("i =", i)
#     i += 1

# i = 2
# while i < 21:
#     print(i)
#     i += 2

# n = int(input("Укажите колличество символов: "))
# i = 0
# while i < n:
#     print("*", end="")
#     i += 1

# n = int(input("Укажите колличество символов: "))
# while n > 0:
#     print("*", end="")
#     n -= 1

# нахождение суммы всех целых нечетных чисел в диапазоне , указанном пользователем
#
# start = int(input('Start: '))
# end = int(input('End: '))
# i = start
# sum_ = 0
# while i <= end:
#     if i % 2:
#         sum_ += i
#     i += 1
# print('Summa: ', sum_)

#
# n = input("Введите целое число: ")
#
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("Число не целое!")
#         n = input("Введите целое число: ")
# if n % 2 == 0:
#     print("Четное число")
# else:
#     print("Нечетное число")

# i = 0
# while i < 10:
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
# print("\nЦикл завершен!")

# i = 0
# while i < 10:
#     if i == 5:
#         i += 1
#         continue
#     print(i, end=" ")
#     i += 1
# print("\nЦикл завершен!")

# i =0
# while True:
#     print(i)
#     if i == 5:
#         break
#     i += 1

# while True:
#     n = int(input("Введите положительное число: "))
#     if n < 0:
#         break
# print("Цикл завершен")

# Произведение чисел пока не введете 0
# m = 1
# while True:
#     n = int(input("Введите число: "))
#     if n == 0:
#         break
#     m *= n
# print("Произведение: ", m)

# i = 0
# while i < 10:
#     if i == 5:
#         break
#     print(i)
#     i += 1
# else:
#     print("Цикл окончен, i =", i)

# -----------------------------------------------------------------------
# kol = int(input("Введите колличество чисел последовательности: "))
# i = 1
# ch = float(input("Введите число: "))
# min_ch = ch
# max_ch = ch
# sum_ch = ch
# while i < kol:
#     ch = float(input("Введите число: "))
#     sum_ch += ch
#     if ch < min_ch:
#         min_ch = ch
#     if ch > max_ch:
#         max_ch = ch
#     i += 1
#
# print("Колличество чисел: ", kol)
# print("Минимальное число: ", min_ch)
# print("Максимальное число: ", max_ch)
# print("Среднее арифметическое: ", sum_ch / kol)

# i = 1
# while i < 5:
#     print("Внешний цикл: i =", i)
#     j = 1
#     while j < 4:
#         print("\t Внутренний цикл: j =", j)
#         j += 1
#     i += 1
# -------------------------------------------------------------------------

# i = 1
# while i <10:
#
#     j = 1
#     while j < 10:
#         print(i, "*", j, "=", i*j, "\t\t", end="")  # строка
#         j += 1
#     print()
#     i += 1

# for !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# видео Python, 13.12.2022, 7 пара

# for element in collection:
#       тело цикла

# for i in 'Hello':
#     print(i)

# for color in 'red', 'orange', 'yellow', 'green', 1, 20, 0.3:
#     print("color:", color)


# range(start, stop, step) - только целые числа  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# print(range(1, 3))

# for i in range(0, 21, 2):    # от 0 до 21 но показываются цифры с шагом 2
#     print(i, end=" ")
#
# print("\nтоже самое что и for сверху:")
# i = 0
# while i <= 20:
#     print(i, end=" ")
#     i += 2

# так же for с отрицательным шагом, тогда число start должно быть, больше числа stop

# for i in range(11, 2, -1):
#     print(i, end=" ")
#
# print()
# i = 11
# while i > 2:
#     print(i, end=" ")
#     i -= 1

# for i in range(100, 0, -10):
#     print(i, end=" ")

#                                      Пользователь вводит целое число.
# Необходимо вывести все целые числа, на которое заданное число делится без остатка.

# a = int(input("Введите целое число: "))  # 36
# for i in range(1, a + 1):
#     if a % i == 0:
#         print(i, end=" ")
# otvet=1 2 3 4 6 9 12 18 36

# Вывести целые числа в диапазоне от 10 до 100 у которых есть две одинаковые цифры.
# 11 22 33 44 55 66 77 88 99

# 1 variant
# for i in range(10, 100):     # 12 => 2 ==1
#     a = i % 10  # ostatok ot deleniya: posle zapyatoi
#     b = i // 10 # celochislenoe delenie: do zapyatoi
#     if a == b:
#         print(i, end=" ")

# 2 variant
# for i in range(11, 100, 11): # nachinaem s 11 i berwm kazdoe 11oe chislo
#     print(i, end=" ")

# for i in range(3):
#     if i == 1:
#         continue  # break
#     print(i)
# else:
#     print('done')
# resultat=0 2 done

# for i in range(3): # диапазон от 0 до 3
#     print("++++", i)
#     for j in range(2):
#         print("----", j)

# Вывести на экран прямоугольник из звездочек, ширину и высоту задает пользователь
# w = int(input("Введите длину прямоугольника: "))
# h = int(input("Введите высоту прямоугольника: "))
#
# for i in range(h):
#     for j in range(w):
#         print("*", end="")
#     print()

# Вывести пустой прямоугольник, для описания контура фигуры использовать звездочки:

# w = int(input("Введите длину прямоугольника: "))
# h = int(input("Введите высоту прямоугольника: "))
#
# for i in range(h):
#     for j in range(w):
#         if i == 0 or i == h - 1 or j == 0 or j == w - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()
# resultat= if w = 16 and h = 4 = ****************
#                                 *              *
#                                 *              *
#                                 ****************

# letter = [i for i in "Hello"]
# print(letter)
# resultat = ['H', 'e', 'l', 'l', 'o']

# num = [i for i in range(30) if i % 2 == 0]
# print(num)


# !!!!!!!!!!!!!!!!     Spiski "spisok"          !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


# nums = [8, 3, 9, 4, 1]  # index minusovoi schitaetsya s conca spiska do nachala (video:(Python, 13.12.2022, 7 пара) 01h:15min)
# print(nums)
# print(id(nums))               # id spiska ne menyaetsa
# print(type(nums))
# print(nums[0])
# print(nums[2])
# print(nums[-1])
# print(nums[-5])
# #zamena elementov v indekse
# nums[1] = 256
# print(nums)
# print(id(nums[1]))               # id spiska ne menyaetsa
# nums[3] += 100
# print(nums)

# nums = [8, 3, 9, 4, 1]
# print(nums)
# print("Длина списка: ", len(nums))

# sozdaem pustoi spisok:
# s = []
# print(s)
#
# s1 = list()
# print(s1)
#
# s2 = list("Hello")
# print(s2)
# -----

# s = [1, 3, 5]
# print(s)
# n = s * 6
# print(n)

# n = list(range(2, 10, 3))
# print(n)

# n = 5
# a = [2 for i in range(n)]
# print(a)
#
# n = 5
# a = [i for i in range(n)]
# print(a)

#
# n = 5
# a = [i ** 2 for i in range(1, n+1)]
# print(a)

# c = [i * 3 for i in "list"]
# print(c)

# a = [1, 2, 3]
# b = [4, 5]
# c = a + b
# print(c)
# d = a * 2
# print(d)

# a = [0] * int(input("Введите количество элементов списка: "))
# print(a)
# for i in range(len(a)):
#     a[i] = input("->")
# print(a)

# a = [int(input("->")) for i in range(int(input("Введите количество элементов списка: ")))]
# print(a)

# !!!!!!!!!!!!!!!!!!            2 sposoba raboti "for"         !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# a = [8, 4, 2, 9, 1]
# #1=
# for i in range(len(a)):  #0 1 2 3 4 - po indexsam
#     print(a[i], end=" ")
#
# print()
#
# #2=
# for elem in a   # 8, 4, 2, 9, 1  - po znacheniu elementov
#     print(elem, end=" ")

# video Python, 13.12.22  8 para

# poschitat v spiske summu vsex otricatelnix elementov (spisok vvodit polsovatel):

# a = [int(input("Введите элемент списка: ")) for i in range(int(input("Введите длину списка: ")))]
# print("Список: ", a)
#
# s = 0
# # for i in range(len(a)):
# #     if a[i] < 0:
# #         s += a[i]
#
# for i in a:
#     if i < 0:
#         s += i
# print("Сумма отрицательных элементов", s)


# sp = list(range(21, 41))                      # or      sp = [i for i in range(21, 41)]
# print(sp)
# ch = 0
# nech = 0
# for i in sp:
#     if i % 2 == 0:
#         ch += 1
#     else:
#         nech += i
# print("Количество четных элементов списка:", ch)
# print("Сумма нечетных элементов:", nech)

# Naiti sredne arifmeticheskoe vsex nenulevix elementov vvedennogo spiska

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print("Список: ", a)
#
# n = 0
# summa = 0
# for i in a:
#     summa += i
#     if i != 0:
#         n += 1
# print("Среднеарифметическое:", summa/n)

# dan spisok chisel. vivedite vse elementy spiska, kotorie bolse predidusego elementa.
# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print("Список: ", a)
# for i in range(1, len(a)):
#     if a[i] > a[i - 1]:
#         print(a[i], end=" ")


# video Python, 13.12.2022, 9 пара !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1

# a = [7, 8, 2, 1, 17]
# print(a)
# a[0], a[-1] = a[-1], a[0]
# print(a)
# resultat: [7, 8, 2, 1, 17]
#           [17, 8, 2, 1, 7]

# srez "срез" !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# name spisok[start:stop:step]

# a = [7, 8, 2, 1, 17, 9]
# print(a[1:4])
# print(a[::2])  # vivoditsya kazdii vtoroi element iz spiska
# print(a[::-1])
# print(a[-2:2:-1])
# print(a[:-2])
# print(a[10:20]) # sozdaetsya new spisok pustoi bez oshibok


# s = list(range(1, 8))
# print(s)
# print(s[::-1])
# print(s[::2])
# print(s[1::2])
# print(s[:1])
# print(s[-1:])
# print(s[3:4])
# print(s[4:]) # or print(s[-3:])
# print(s[-3:1:-1])
# print(s[2:5])


# a = [7, 8, 2, 1, 17, 9]
# a[1:3] = [0, 0, 0, 0]
# print(a)
# a[1:2] = [20]
# print(a)
# a[2] = 50
# print(a)
# del a[2]
# print(a)
# del a[2:4]
# print(a)
# del a[:]
# print(a)


# methody spiskov "Методы списков" !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# append(), extend()
# video Python, 13.12.2022, 9 пара (29 minuts)
# print(dir(list))

# s = [7, 8, 2, 1, 17, 9]
# print(s)
# s.append(99)  # dobavlyaet odin element v konec spiska
# print(s)
# s.extend([1, 2, 3])  # dobavlyaet spisok elementov v konec pervonachalnogo spiska
# print(s)
# s.extend('add')
# print(s)
# s.insert(2, 100)  # dobavlyaet element v spisok (vo vtoroi index). Первый параметр это индекс,
#                    # второй пар.-добавляемое значение
# print(s)


# a = [int(input("Введите элемент списка: ")) for i in range(int(input("Введите длину списка: ")))]

# a = []
# n = int(input("n = "))
# for i in range(n):
#     # x = int(input(" -> "))
#     # a.append(x)
#
#     a.append(int(input("-> ")))
# print(a)

# [a.append(int(input("Введите элемент списка: "))) for i in range(int(input("Введите длину списка: ")))]
# print(a)


# Polzovatel vvel chisla kratnie 3, proveryat deistvitelno li ono kratnoe 3. Esli da to dobavit v spisok, esli
#net, to vivodit polzovatelu na ekrane - ne delitsya na 3 bez ostatka

# a = []
# n = int(input("Кол-во элементов списка: "))
# for i in range(n):
#     x = int(input("Введите число кратное 3: "))
#     if x % 3 == 0:
#         a.append(x)
#     else:
#         print(x, "не делится на 3 без остатка")
# print(a)


# iz dvux spiskov poisk odinakovix elementov
# a = [5, 9, 2, 1, 4, 3, 2, 4]
# b = [4, 2, 1, 3, 7]
# c = []
# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
#             break
# print(c)
