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

num = 4321
res = num % 10 * 1000
num //= 10
res += num % 10 * 100
num //= 10
res += num % 10 * 10
num //= 10
res += num % 10
print(res)
