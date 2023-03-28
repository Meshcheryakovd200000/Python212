# Регулярные выражения
import re

# s = "Я ищу совпадения в 2023 году. И я их найду в 2 счёта. 9812. [Hello]"
#
# # reg = r'[А-яёЁ.]'
# reg = r'[А-яёЁ.\[\]]'
# reg = r'[^0-9]'  # все что угодно кроме цифр
# # reg = r'[A-z]'
# print(re.findall(reg, s))
# print(ord("Я"))
# print(ord("а"))

# ---
# zadacha
# Найти время в формате [16:25]

# s1 = "Час в 24-часовом формате от 00 до 23. 2021-06-15Т21:45. Минуты, в диапазоне от 00 до 59. 2021-06-15Т01:09"
# r1 = '[0-2][0-9]:[0-5][0-9]'
# print(re.findall(r1, s1))

# ---

# s = "Я ищу совпадения в 2023 году. И я их найду в 2 счёта. 98_12. [Hello]"
# reg = r'\d'  # ищет совпадения с числами 0-9
# reg = r'\w'  # любые буквы не только английские
# reg = r'\A\w\s'
# reg = r'совпадения'
# reg = r'\[Hello\]\Z'
# reg = r'году\.\Z'
# reg = r'ния\b'
# reg = r'ния\b'
# reg = r'\w+'
# reg = r'20*'
# print(re.findall(reg, s))

# d = "Цифры: 7, +17, --42, 0013, 0.3"
# print(re.findall(r'[+-]\d+', d))
# print(re.findall(r'[+-]?\d+', d))
# print(re.findall(r'[+-]*\d+', d))
# print(re.findall(r'[+-]?[\d.]+', d))  # [\d.] - ищется один символ

# d = "05-03-1987 # Дата рождения"
# print("Дата рождения:", re.sub('#.*', '', d))
#
# # Дата рождения: 05-03-1987
# print("Дата рождения:", re.sub('-', '.', re.sub('#.*', '', d)))  # 05.03.1987

# zadacha

# d = "autor=Пушкин А.С.; title = Евгений Онегин; price =200; year= 1831"
# # r1 = r'='
# # r1 = r'\w+='
# # r1 = r'\w+\s*=\s*\w+\s*[\w.]*'
# r1 = r'\w+\s*=[^;]+'
# print(re.findall(r1, d))

# s1 = "12 сентября 2023 года"
# r1 = r"\d{2,4}"  # max значение поиска от 2 цифр до 4 цифры
# print(re.findall(r1, s1))
#
# # zadacha
#
# s1 = "+7 499 456-45-78, +74994564578, 7 (499) 456 45 78, "
# r1 = r"\+?7\d{10}"
# print(re.findall(r1, s1))

# ---

# s = "Я ищу совпадения в 2023 году. И я их найду в 2 счёта. 98_12. [Hello]"

# reg = r'^\w+\s\w+'
# reg = r'^\w+\.$'
# print(re.findall(reg, s))

# print(re.findall(r'\w+', '12 + й'))
# print(re.findall(r'\w+', '12 + й', flags=re.ASCII))


# text = "hello world"
# print(re.findall(r'\w\+', text, re.DEBUG))

# reg = 'я'
# print(re.findall(reg, s, re.IGNORECASE))
#
# text = """
# one
# two
# """
# print(re.findall(r"one.\w+", text))
# # print(re.findall(r"one$", text))
# # print(re.findall(r"one$", text, re.MULTILINE))
# print(re.findall(r"one.\w+", text, re.DOTALL))

# print(re.findall(r"""
# [\w-]+ # part1
# @       # @
# [\w-]+  #part2
# """, "test@mail.ru", re.VERBOSE))  # исключает пробелы

# ---

# text = """Python,
# python,
# PYTHON
# """
# reg = "(?im)^python"
# print(re.findall(reg, text))

# ---

# def validate_name(name):
#     # return re.findall(r'^[\w-]{3,16}$', name)  # $ должны быть только допустимые символы
# ??????    return re.findall(r'^[\w-]{3,16}$', name)[0]  # $ должны быть только допустимые символы
#
#
# print(validate_name('Python_master'))
# print(validate_name('@Pyt'))
# ---

# zadacha

# s1 = "123456@i.ru, 123_456@ru.name.ru, login@i.ru, логин-1@i.ru, login.3@i.ru, login.3-67@i.ru, 1login@ru.name.ru"
# reg = r'[\w.-]+@\w*\.?\w*\.?\w*'
# reg = r'[\w.-]+@[\w.-]+[a-z]{2,3}'
# print(re.findall(reg, s1))

# text = "<body>Пример жадного соответствия регулярных выражений</body>"
# print(re.findall('<.*?>', text))
# # *?, +?, ?? - "ленивое соответствие" захватывает минимальное число символов
#
# s1 = "12 сентября 2023 года"
# r1 = r"\d{3,}?"  #
# print(re.findall(r1, s1))

# t = "<p>Изображение <img alt='картинка' src='bg.jpg'> - фон страницы</p>"
# # reg = r'<img.*?>'
# reg = r'<img\s[^>]*?src\s*=\s*[^>]+>'
# print(re.findall(reg, t))
# ---
# t = "Петр, Ольга и Виталий отлично учатся"
# reg = "Петр|Ольга|Виталий"
# print(re.findall(reg, t))
# ---
t = "int = 4, float = 4.0, double = 8.0f"
# reg = r"((int|double)\s*=\s*(\d+[\w.]*))"
reg = r"(?:int|double)\s*=\s*\d+[\w.]*)"
print(re.findall(reg, t))

# (?: ) - скобки не сохраняющие (группирующие)
