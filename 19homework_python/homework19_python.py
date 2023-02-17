# 1
from random import randint


def bynary_search(s, item):
    first = 0
    last = len(s) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if s[midpoint] == item:
            found = True
        else:
            if item < s[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found


a = [randint(1, 100) for i in range(10)]
print(a)
a.sort()
print(a)
n = int(input("Введите число: "))
if bynary_search(a, n):
    print(f"Число {n} в списке присутсвует")
else:
    print(f"Число {n} в списке отсутствует")
