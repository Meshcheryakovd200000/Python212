# 1 Дана строка, в которой буква h встречается минимум два раза. Удалите из этой строки первое и
# последнее вхождение буквы h, а также все символы, находящиеся между ними.

# s = "I am learning Python. hello, WORLD"
# ind1 = s.find('h')
# ind2 = s.rfind('h')
# res = s[:ind1] + s[ind2 + 1:]
# print(res)

# 2 Дана строка, в которой буква h встречается как минимум два раза. Разверните последовательность символов,
# заключенную между первым и последним появлением буквы h, в противоположном порядке.

# s = "I am learning Python. hello, WORLD"
# ind1 = s.find('h')
# ind2 = s.rfind('h')
# a = s[ind1 + 1:ind2]
# a = a[::-1]
# res = s[:ind1] + a + s[ind2:]
# print(res)

# 3 Найти в строке указанную подстроку и заменить ее на новую.
# Строку, ее подстроку для замены и новую подстроку вводит пользователь.

# a = input("Строка: ")
# b = input("Ее заменяемая посдтрока:")
# c = input("Новая посдтрока:")
#
# print(a.replace(b, c))

# 4 Дана строка, содержащая русскоязычный текст. Найти количество слов, начинающихся с буквы ‘е’.

s = "Ежевику для ежат принеси два ежа. Ежевику еле-еле Ежата возле ели съели."
s = s.lower()
s = s.split()
count = 0

for i in s:
    if i.startswith("е"):
        count += 1
print("Количество слов: ", count)
