# Задача 1: Есть список из 10 элементов, заполненный случайными числами. Необходимо найти число,
# введенное пользователем. Используйте алгоритм линейного поиска.
from random import randint

# def search(s, item):
#     pos = 0
#     found = False
#     while pos < len(s) and not found:
#         if s[pos] == item:
#             found = True
#         else:
#             pos = pos + 1
#     return found
#
#
# a = [randint(1, 100) for i in range(10)]
# a.sort()
# print(a)
# n = int(input("Введите число: "))
# if search(a, n):
#     print(f"Число {n} в списке присутсвует")
# else:
#     print(f"Число {n} в списке отсутствует")

# ----------------

# Задача 2: Удаление строки из файла по ее индексу
# n = int(input("Введите строку которую хотите удалить: "))
#
# f = open('20.txt', mode='w')
# f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;\n")
# f.close()
#
# f = open('20.txt', mode='r')
# list_ = f.readlines()
# print(list_)
# del list_[n]
# print(list_)
# f.close()
#
# f = open('20.txt', mode='w')
# for i in list_:
#     f.write(i)
# f.close()

# ------------------------

# Задача 3: Есть 4 списка целых. Необходимо их объединить в пятом списке.
# Полученный результат в зависимости от выбора пользователя отсортировать
# по убыванию или возрастанию. Найти значение, введенное пользователем, с использованием линейного поиска.


def sort(a):
    if len(a) > 1:
        x = a[(len(a) - 1) // 2]
        low = [i for i in a if i < x]
        eq = [i for i in a if i == x]
        hi = [i for i in a if i > x]
        a = sort(low) + eq + sort(hi)
    return a


def search(s, item):
    pos = 0
    found = False
    while pos < len(s) and not found:
        if s[pos] == item:
            found = True
        else:
            pos += 1
    return found


a1 = [5, 9, 6, 7]
a2 = [3, 11, 8]
a3 = [2, 4]
a4 = [10, 1, 12]
a = a1 + a2 + a3 + a4
print(a)
m = int(input("1 - сортировка по убыванию \n2 - сортировка по возрастанию\nВведите сортировку:\n -> "))

if m == 1:
    a = sort(a)
    a = a[::-1]

else:
    a = sort(a)
print(a)
n = int(input("Введите значение для поиска: "))
if search(a, n):
    print(f"Значение {n} найдено")
else:
    print(f"Значение {n} не найдено")
