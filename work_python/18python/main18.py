# video Python 02.02.2023, 35 пара main18
import re


# (?: ) - скобки не сохраняющие (группирующие)


# s1 = '192.168.255.255'  # 127.0.0.1
# # reg = r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}'
# reg = r'(?:\d{1,3}.){3}\d{1,3}'
# print(re.findall(reg, s1))

# s1 = "Word2016, PS6, AI5"
# reg = r'(([A-z]+)(\d+))'
# reg1 = r'(([A-z]+)(\d+))[0][1]'
# reg2 = r'((\d+))'
# reg3 = r'(([A-z]+))'
# print(re.findall(reg, s1))
# print(re.findall(reg, s1, re.IGNORECASE))
# print(re.findall(reg1, s1))
# print(re.findall(reg2, s1))
# print(re.findall(reg3, s1))
# -----

# s1 = "5 + 7*2 -4"
# reg = r'\s*([+*-])\s*'
#
# print(re.split(reg, s1))
# -----

# 41 минута
# s = '28-08-2021'
# reg = r'^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(19[0-9]|20[0-9][0-9])$'  # (0[1-9]|[12][0-9]|3[01])-день
# # (0[1-9]|1[0-2])- месяц (19[0-9]|20[0-9][0-9]) - год
# print(re.findall(reg, s))
# print(re.search(reg, s))
# ---

# s = "Я ищу совпадения в 2023 году. И я их найду в 2 счёта. 9812"
# reg = r'([0-9]+)\s(\D+)'
# print(re.findall(reg, s)[0])
# print(re.search(reg, s).group(1))
# m = re.search(reg, s)
# print(m[0])
# print(m[1])
# print(m[2])
# -----

# text = """
# Самара
# Москва
# Тверь
# Уфа
# Казань
# """
# count = 0
#
#
# def repl_find(m):
#     global count
#     count += 1
#     return f"<option value='{count}'>{m.group(1)}</option>\n"
#
#
# print(re.sub(r'\s*(\w+)\s*', repl_find, text))
# print(re.findall(r'\s*(\w+)\s*', text))

# -----

# s = "<p>Изображения <img src='bg.jpg'> - фон страницы</p>"
# reg = r"<img\s+[^>]*src=(?P<q>['\"])(.+)(?P=q)>"
# print(re.findall(reg, s)[0][1])

# (?P<name>) (?Pname)  video 36пара 01 час

# s = "Самолет прилетает 10/23/2023. Будем вас рады видеть после 10/24/2023"  # 24.10.2023
#
# reg = r"(\d{2})/(\d{2})/(\d{4})"
# # (\d{2}) - поиск 2 цифр
# # (\d{4}) - поиск 4 цифр
# print(re.sub(reg, r"\2.\1.\3", s))  # sub()-поиск и замена элемента
# \2 - это номер 2ой круглой скобки = (\d{2}), r (row) -строка

# s = "yandex.com and yandex.ru"
# reg = r'(([a-z0-9\-]{2,}\.)+[a-z]{2,4})'
# # {2,}\. - от двух и более символов, после символов должна стоять точка
# # может быть домен более 2 и 3 уровня то ищется по шаблону еще символы a-z от 2 раз
# print(re.sub(reg, r"http://\1", s))


# --------------------------------------------------------------------------------------------------------------
# Рекурсия
# ------------------------------------------------------------------------------------------------------------
# video Python, 02.02.2023, 36 пара main18, 18:25

# def elevator(n):
#     if n == 0:
#         print("Вы в подвале")
#         return
#     print("->", n)
#     elevator(n - 1)  # 5 4 3 2 1 сохранилась в стек
#     print(n, end=" ")  # 1 2 3 4 5
#
#
# n1 = int(input("На каком вы этаже: "))  # 5
# elevator(n1)


# -----------

# video 34 minuta

# def sum_list(lst):
#     res = 0
#     for i in lst:
#         res += i
#     return res
#
#
# print(sum_list([1, 3, 5, 7, 9]))  # 25
# ---

# решение с помощью рекурсии:
# def sum_list(lst):  # 1 шаг итерации: [1, 3, 5, 7, 9], 2 шаг итерации: [3, 5, 7, 9], 3 шаг итерации:[5, 7, 9],
#     # 4 шаг итерации:[7, 9], 5 шаг итерации: [9]
#     if len(lst) == 1:
#         print(lst, "=> lst[0]:", lst[0])
#         return lst[0]
#     else:
#         print(lst, "=> lst[0]:", lst[0])
#         return lst[0] + sum_list(lst[1:])  # записываются в стек 1 3 5 7 9 т.е.
#         # сложение дальше (9+7) = (16+5) = (21+3) = (24+1) = 25
#
#
# print(sum_list([1, 3, 5, 7, 9]))  # 25

# -----

# video 54 minuts

# def to_str(n, base):  # 7
#     convert = "0123456789"
#     if n < base:
#         return convert[n]  # '7'
#     else:
#         return to_str(n // base, base) + convert[n % base]  # '9' '6'
#
#
# print(to_str(769, 10))


# -----

# video 37 пара main19

def to_str(n, base):  # base - основание системы счисления, n - число -254
    convert = "0123456789ABCDEF"
    if n < 0:
        convert = convert[0] + convert[:0:-1]
        if n * (-1) < base:
            return "-" + convert[n]
        else:
            return to_str((n // base) + 1, base) + convert[(n % base)]
    else:
        if n < base:
            return convert[n]
        else:
            return to_str(n // base, base) + convert[n % base]
            # -254/10=25


print(to_str(-254, 10))

print(int('FE', 16))
