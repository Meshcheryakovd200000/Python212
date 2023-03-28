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

n = int(input("Введите колличество ворон: "))
if 0 <= n <= 9:
    print("На ветке", n, end=" ")
    if n == 1:
        print("ворона")
    if 2 <= n <= 4:
        print("вороны")
    else:               # if 5 <= n <= 9 or n == 0:
        print("ворон")
else:
    print("Ошибка ввода данных")

