# 1.1
# a = [0] * int(input("Введите длину списка: "))
# print(a)
# for i in range(len(a)):
# a[i] = input("Введите элемент списка: ")

# 1.2
# a = [int(input("Введите элемент списка: ")) for i in range(int(input("Введите длину списка: ")))]
# print("Список: ", a)
#
# b = []
# for i in range(len(a)):
#     if a[i] > 0:
#         b.append(a[i])
# print("Новый список, состоящий из положительных элементов", b)
#
# s = 0
# q = 0
# for i in b:
#     for j in b:
#         if i > j:
#             s = i
#         if j > i:
#             q = j
# if s > q:
#     print("Наибольший элемент списка: ", s)
# else:
#     print("Наибольший элемент списка: ", q)

# -----------------------------------------------------------------------------------------------

# 2

# w = [int(input("Введите элемент списка: ")) for i in range(int(input("Введите длину списка: ")))]
# print("Список: ", w)
#
# k = int(input("Ведите индекс: "))
# print("k = ", k)
# c = int(input("Введите значение: "))
# print("c = ", c)
#
# w.insert(k, c)
# print(w)


# 3

z = []
for i in range(1, 11):
    # print(i, end=" ")
    z.append(i*i)
# print()
print(z)
