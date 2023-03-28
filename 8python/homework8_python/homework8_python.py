# 1) Введите статистику частотности символов в кортеже
# s = tuple(input("Введите по порядку, без пробелов, элементы кортежа: "))
#
# print("Количество 2 =", s.count('2'))
# print("Количество 5 =", s.count('5'))
# print("Количество 3 =", s.count('3'))
# print("Количество 6 =", s.count('6'))
# print("Количество 1 =", s.count('1'))

# 2)

# lst1 = [1, 2, 3, 3, 2]
# lst2 = [2, 1, 3, 1, 2, 5, 5, 9, 2, 0, 0]
#
#
# def lst_reverse(lst):
#     lst.reverse()
#     unique = []
#     for i in lst:  # [::-1]:
#         if i not in unique:
#             unique.append(i)
#     return tuple(unique)
#
#
# print(lst_reverse(lst1))
# print(lst_reverse(lst2))

# 3) Поиск заданного элемента в кортеже

t = ('ab', "abcd", 'cde', 'abc', 'def')
# print(type(t))
s = input("s = ")

if s in t:
    print("Yes")
else:
    print("Такого элемента нет")
