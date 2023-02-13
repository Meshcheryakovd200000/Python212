# def changeCharToStr(s, c_old, c_new):
#     s2 = ""
#     i = 0
#     while i < len(s):
#         if s[i] == c_old and (i % 2 == 0):
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
# print(str2)


# 2 Удаление цифры, заданной номером позиции

# s = '0123456789'
# print("s = ", s)
# i = int(input("Введите номер позиции: "))
# s2 = s[:i] + s[i+1:]
# print("s2 = ", s2)

# 3 Удаление всех вхождений заданного символа из строки

# i = input("Введите символ: ")
#
#
# def str_old(s):
#     s2 = ""
#     print("s = ", s)
#     for x in s:
#         if x not in i:
#             s2 = s2 + x
#     return s2
#
#
# s2 = str_old("012345363738494")
# print("s2 = ", s2)

# 4

i = int(input("Введите десятичное число: "))
print(bin(i)[2:])
