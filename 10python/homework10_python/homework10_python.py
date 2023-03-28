# 1)
# a = ["red", "green", "blue"]
# print(a)
# print(type(a))
# b = ["#FF0000", "#008000", "#0000FF"]
# print(b)
# print(type(b))
#
# d = dict(zip(a, b))
# print(d)
# print(type(d))


# 2)Создать словарь,в котором ключами будут числа от 1 до 10, а значениями эти же числа,
# возведенные в куб.

# d = dict()
# d = {key: key**3 for key in range(1, 11)}
# print(d)
# print(type(d))


# --------------------

# 3)

# d1 = {1: 10, 2: 20}
# d2 = {3: 30, 4: 40}
# d3 = {5: 50, 6: 60}
#
# d = d1 | d2 | d3
# print(d)


# ---------------------

# 4) Дан словарь {'emp1': {'name': 'Jhon', 'salary': 7500}, 'emp2': {'name': 'Emma', 'salary': 8000},
#      'emp3': {'name': 'Brad', 'salary': 6500}}. Изменить значение зарплаты Brad с 6500 до 8500.

# d = {
#     'emp1': {'name': 'Jhon', 'salary': 7500},
#     'emp2': {'name': 'Emma', 'salary': 8000},
#     'emp3': {'name': 'Brad', 'salary': 6500},
# }
# print(d)
#
#
# namex = input("Введите имя сотрудника: ")
#
# new_salary = int(input("Новое значение зарплаты сотрудника: "))
#
# for key, value in d.items():
#
#     for key1, value1 in value.items():
#
#         if value1 == namex:
#             value['salary'] = new_salary
#
# print(d)


# 5)Пользователь вводит данные о количестве студентов, их фамилии, имена и балл для каждого.
# Программа должна определить средний балл и вывести фамилии и имена студентов, чей балл выше среднего.

# students = dict()
# number_students = int(input("Количество студентов: "))
# s = 0
# for i in range(number_students):
#     name = input(str(i + 1) + " -й студент: ")
#     ball = int(input("Балл: "))
#     students[name] = ball
#     s += ball
# Average_score = s /number_students
# print("\nСредний балл: ", round(Average_score), ". Студенты с баллом выше среднего:")
# for i in students:
#     if students[i] > Average_score:
#         print(i)


# 6) Используя два списка данных, создайте новый словарь с использованием генератора словарей

a = ['color', 'fruit', 'pet']
b = ['blue', 'apple', 'dog']

d = {k: v for k, v in zip(a, b)}
print(d)


