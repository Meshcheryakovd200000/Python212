from random import randint, randrange


# 1

# a = [int(input("Введите элемент списка: ")) for i in range(int(input("Ведите количество элементов списка: \nn = ")))]
# print(a)
#
# ch = int(input("Введите число: \n ch = "))
# if ch in a:
#     ind = a.index(ch)
#     print("Число присутствует в элементах списка")
# else:
#     print("Такого числа в списке нет")
# ------------------------------------------------------------------------

# 2

# from random import randint, randrange

# mas = [randint(0, 100) for i in range(20)]
# print(mas)
# print("Summa:", sum(mas))
# ------------------------------------------------------------------------

# 3

# mas = [randint(0, 100) for i in range(10)]
# print(mas)
# mas.sort(reverse=True)
# print(mas)
# ----------------------------------------------------------------------

# 4

w, h = 3, 4
z = 1
# matrix = [[q for x in range(w)] for y in range(h)]
matrix = []
for y in range(h):
    new_row = []
    for x in range(w):
        q = randint(0, 4)
        new_row.append(q)
        if q != 0:
            z = z * new_row[x]
    matrix.append(new_row)
# print(matrix)

for h in matrix:
    for w in h:
        print(w, end="\t\t")

    print()
print()

print("Произведение ненулевых элементов: ", z)


# 5

