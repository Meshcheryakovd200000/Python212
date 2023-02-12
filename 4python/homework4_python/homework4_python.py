# 1 линия из символов


# kol = int(input("Количество символов: "))
# sim = input("Тип символа: ")
# print("0 - горизонтальная")
# print("1 - вертикальная")
# ori = int(input("ориентация линии: "))
# i = 0
# while ori == 0:
#     if i < kol:
#         print(sim, " ", end="")
#         i += 1
#         if i == kol:
#             break
# while ori == 1:
#     if i < kol:
#         print(sim)
#         i += 1
#         if i == kol:
#             break

# -----------------------------------------

# 2 прямоугольник из чередующихся символов

# gor_str = 0
# vert = 5
#
# while gor_str < vert:
#     j = 0
#     while j < 16:
#         if gor_str % 2 == 0:
#             print("+", end="")
#             j += 1
#         if gor_str % 2 == 1:
#             print("-", end="")
#             j += 1
#     print()
#     gor_str += 1


# 3 находим max значение из трех чисел введенных
# пользователем (с использованием тернарного выражения)

# a = int(input())
# b = int(input())
# c = int(input())
# maxim = a if b < a > c else b if a < b > c else c
# print("Максимальное значение: ", maxim)


# 4 Калькулятор

print("Выберите операцию:")
print("1 - 'r' - применяет унарный минус к операнду")
print("2 - '+' - сложение")
print("3 - '-' - вычитание")
print("4 - '/' - деление")
print("5 - '*' - умножение")
print("6 - '%' - деление по модулю (остаток от деления)")
print("7 - '<' - минимальное из двух чисел")
print("8 - '>' - максимальное из двух чисел")

cifra = int(input("Введите цифру от 1 до 8(включительно): "))

while 1 > cifra > 8:
    print("")



res = 1

while 1 <= cifra <= 8:
    ch1 = int(input("Введите первое число: "))
    ch2 = int(input("Введите второе число: "))
    if cifra == 1:
        ch1 = -ch1
        ch2 = -ch2
        print("Унарный минус первого числа: ", ch1)
        print("Унарный минус второго числа: ", ch2)
        break
    if cifra == 2:
        res = ch1 + ch2
        print(res)
        break
    if cifra == 3:
        res = ch1 - ch2
        print(res)
        break
    if cifra == 4:
        res = ch1 / ch2 if ch2 != 0 else "На 0 делить нельзя"
        print(res)
        break
    if cifra == 5:
        res = ch1 * ch2
        print(res)
        break
    if cifra == 6:
        res = ch1 % ch2
        print(res)
        break
    if cifra == 7:
        res = ch1 if ch1 < ch2 else ch2
        print(res)
        break
    if cifra == 8:
        res = ch2 if ch2 > ch1 else ch1
        print(res)
        break

