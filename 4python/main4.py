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

# преобразуем число 4321 в 1234
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


# тернарные выражения

# a, b = 10, 5
# minim = "a == b" if a == b else "a > b" if a > b else "b > a"
# print(minim)

# a, b = 10, 0
# c = a / b if b != 0 else "На ноль делить нельзя"
# print(c)

# Исключения

# пример ошибок:
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





# Цикл while +++++++++++++++++++++++++++++++++++++++++++++++++++++++

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

# n = int(input("Укажите количество символов: "))
# i = 0
# while i < n:
#     print("*", end="")
#     i += 1

 # q = int(input("Укажите количество символов: "))
 # while q > 0:
 #     print("*", end="")
 #     q -= 1

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

# таблица умножения
# i = 1
# while i <10:
#
#     j = 1
#     while j < 10:
#         print(i, "*", j, "=", i*j, "\t\t", end="")  # строка
#         j += 1
#     print()
#     i += 1

