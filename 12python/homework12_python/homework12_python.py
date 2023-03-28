def func_compute(n):
    def inner(x):
        return n * x

    return inner


res = func_compute(2)
print(res(15))
print(res(20))
res = func_compute(3)
print(res(15))
print(res(20))

# --------------------------------
# 2

print()
print("lambda выражение, которое возвращает произведение трех чисел: 2, 5, 5 = ")
print((lambda x, y, z: x * y * z)(2, 5, 5))

# --------------------------------
# 3
students = [
    {'name': 'Jennifer', 'final': 95},
    {'name': 'David', 'final': 92},
    {'name': 'Nikolas', 'final': 98}
]

print()
print("Отсортировать список объектов по имени студентов и итоговым оценкам в порядке убывания:")
result = sorted(students, key=lambda item: item['name'])
print(result)
result = sorted(students, key=lambda item: item['final'], reverse=True)
print(result)

# -----------------------
# 4

print()
print("Получить минимальную и максимальную итоговую оценку студентов:")
result = min(students, key=lambda item: item['final'])
print(result)
result = max(students, key=lambda item: item['final'])
print(result)


# a = students[0]
# print(a)
# b = students[1]
# c = students[2]
#
# print((lambda a, b, c: a if a < b and a < c else b if b < c else c)(a['final'], b['final'], c['final']))
# print((lambda a, b, c: a if a > b and a > c else b if b > c else c)(a['final'], b['final'], c['final']))
