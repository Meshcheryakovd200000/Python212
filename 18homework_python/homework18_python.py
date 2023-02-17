import re

# Задача 1 Валидация номера телефона:
def validate_phone(number):
    reg = r"^\+?7\s*\(?\d{3}\)?\s*[\d\s-]{7,9}$"
    return re.search(reg, number).group()
    # return re.findall(reg, number)[0]


print(validate_phone('+7 499 456-45-78'))
print(validate_phone('+74994564578'))
print(validate_phone('7 (499) 456 45 78'))
print(validate_phone('7 (499) 456-45-78'))


# 2 Задачу необходимо решить с использованием рекурсии:
# Вычислить количество отрицательных чисел в списке

# def negative(a):
#     if not a:  # len(a) == 0 a == []
#         return 0
#     else:
#         count = negative(a[1:])
#         if a[0] < 0:
#             count += 1
#         return count
#
#
# lst = [-2, 3, 8, -11, -4, 6]
# print(lst)
# n = negative(lst)
# print("n = ", n)  # 3
