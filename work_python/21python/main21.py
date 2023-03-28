# video 41 пара
# ---------------------------------------------------------
# Файлы - продолжение
# --------------------------------------------------------

# f = open("text1.txt", "r")
# print(f.read(3))
# print(f.tell())
# print(f.seek(1))
# print(f.read())
# print(f.tell())
# f.close()
# ---

# f = open("text1.txt", "r+")
# print(f.write("I am learning Python"))
# print(f.seek(3))
# print(f.write("-new string-"))
# print(f.tell())
# f.close()
# ---

# with open('text3.txt', 'w+') as f:
#     print(f.write('0123456789\n123456789'))
#
#
# with open('text3.txt', 'r') as f:
#     for line in f:
#         print(line[:6])

# запись в файл вещественных чисел:

# file_name = "res_1.txt"
# lst = [4.5, 2.8, 1.0, 0.3, 4.33, 7.777]
#
#
# def get_line(lt):
#     lt = list(map(str, lt))  # преобразование из списка вещественных в строковое
#     print(lt)
#     return '\t'.join(lt)  # объединит через пробел
#
#
# with open(file_name, 'w') as f:  # f - имя нашего файла
#     f.write(get_line(lst))
#
#     # get_line(lst)
# print("Done!")

# Задача: В текстовом файле хранятся вещественные числа. Вывести их на экран и вычислить их количество.

# file_name = "res_1.txt"
#
# numbers = [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 7.777]
#
#
# def get_string(l: list) -> str:
#     return '\t'.join(map(str, l))
#
#
# with open(file_name, 'r+', encoding='utf-8') as file:
#     # text = get_string(numbers)
#     # file.write(text)
#     nums = file.read()  # считываем данные
#     print(nums)
#     nums_list = list(map(float, nums.split('\t')))  # разбиение данных
#     print(nums_list)
#     print(len(nums_list))
#     print(sum(nums_list))

# Задача: Написать функцию, которая выводит слово из файла, имеющее максимальную длину
# (или список слов, если таковых несколько).

# def longest_world(file):
#     with open(file, 'r', encoding='utf-8') as text:
#         w = text.read().split()
#         max_length = len(max(w, key=len))
#         res = [word for word in w if len(word) == max_length]
#         if len(res) == 1:
#             return res[0]
#         return res
#
#
# file_name = "res_2.txt"
# print(longest_world(file_name))


# text = "Строка №1\nСтрока №2\nСтрока №3\nСтрока №4\nСтрока №5\nСтрока №6\nСтрока №7\nСтрока №8\nСтрока №9\nСтрока №10\n"
#
# with open('one.txt', 'w') as f:  # создался файл one.txt
#     f.write(text)

# read_file = 'one.txt'
# write_file = 'two.txt'
# with open(read_file, 'r') as fr, open(write_file, 'w') as fw:
#     for line in fr:
#         line = line.replace("Строка", "Линия - ")  # replace() - поиск и замена, берем строку из файла 'one.txt'
#         # изменяем её и вставляем в файл 'two.txt'
#         fw.write(line)

# ----------

# video 41 пара main 21, 01час : 04 минут

# Работа с путями
# Модуль OS (OS.PATH) - Объединение путей

import os
import time

# import os.path

# print(os.getcwd())  # возвращает путь к текущей директории
# print(os.listdir())  # возвращает список папок и файлов, находящихся в текущей директории
# print(os.listdir("../.."))


# os.mkdir("folder")  # создает директорию "folder" по указанному пути
# os.makedirs("nested1/nested2/nested3")  # создает не только конечную директорию, но и промежуточные папки

# os.remove("xyz.txt")  # удаление файла

# os.rename("nested1", "test")  # переименование папок и файлов

# os.rename("text1.txt", "test/text1.txt")  # все промежуточные директории должны существовать обязательно

# os.renames("text1.txt", "text/text.txt")  # создаются промежуточные директории

# video 42 пара
# os.rmdir("folder")  # удаление пустой директории
# ---


# for root, dirs, files in os.walk("test", topdown=False):  # topdown=True - сверху вниз, topdown=False - снизу вверх
#     print("Root:", root)  # корневая папка
#     print("Sub_dirs:", dirs)  # дочерняя папка
#     print("Files:", files)  # файлы в каталогах
# ---


# Удаление пустых директорий в ветви

# def remove_empty_dirs(root_tree):
#     print(f"Удаление пустых директорий в ветви {root_tree}")
#     print("-" * 50)
#     for root, dirs, files in os.walk(root_tree):
#         if not os.listdir(root):
#             os.rmdir(root)
#             print(f"Директория {root} удалена.")
#     print("-" * 50)
#
#
# remove_empty_dirs("test")
# ---

os.path

# print(os.path.split(r'D:\Python212\Python\work_python\21python\test\nested2\nested3\xyz1.txt')[1])  # разбивает путь
# на кортеж (head, tail)
# print(os.path.dirname(r'D:\Python212\Python\work_python\21python\test\nested2\nested3\xyz1.txt'))  # имя директории
# print(os.path.basename(r'D:\Python212\Python\work_python\21python\test\nested2\nested3\xyz1.txt'))  # имя файла

# print(os.path.join('D:\Python212', 'Python', 'work_python', '21python', 'xyz12345.txt'))  # соединяет один или
# несколько компонентов пути с учетом особенностей OS

# ---

# Задача:
# video 42 пара, main21, 31 minuta

# # dirs = [r'Work\F1', r'Work\F2\F21']
# # for d in dirs:
# #     os.makedirs(d)
#
# files = {
#     'Work': ['w.txt'],
#     r'Work\F1': ['f11.txt', 'f12.txt', 'f13.txt'],
#     r'Work\F2\F21': ['f211.txt', 'f212.txt']
# }  # словарь
#
# for d, file in files.items():  # d-ключ(директория), file-значение(файл)
#     for f in file:  # проходит объединение путей Work\F1\f11.txt, потом Work\F1\f12.txt, потом Work\F1\f13.txt и т.д.
#         file_path = os.path.join(d, f)
#         # print(file_path)
#         open(file_path, 'w').close()  # создаем файлы с помощью open() и сразу закрыли close()
#
# file_with_text = [r'Work\w.txt', r'Work\F1\f12.txt', r'Work\F2\F21\f211.txt', r'Work\F2\F21\f212.txt']  # пути на файлы
# # в которые будем записывать данные
#
# for file in file_with_text:  # file - переменная которой будем проходиться по списку file_with_text
#     with open(file, 'w') as f:
#         f.write(f"some sample text for {file} file")
#
#
# def print_tree(root, topdown):
#     print(f"Обход {root} {'сверху вниз' if topdown else 'снизу вверх'}")
#     for root, dirs, fl in os.walk(root, topdown=topdown):
#         print(root)
#         print(dirs)
#         print(fl)
#     print('-' * 50)
#
#
# print_tree('Work', topdown=False)
# print_tree('Work', True)

# ---

# print(os.path.exists(r'D:\Python212\Python\work_python\21python\test\nested2\nested3\xyz1.txt'))  # exists- возвращает
# True, если путь указывает на существующий путь в файловой системе

path = r'D:\Python212\Python\venv\Scripts\python.exe'
k_size = os.path.getsize(path)  # размер файла
print(k_size // 1024)
# print(os.path.getmtime(path))  # время последнего изменения файла
t1 = os.path.getmtime(path)
print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(t1)))  # # t1 время последнего изменения файла
# print(os.path.getatime(path))  # время последнего доступа к файлу
t2 = os.path.getatime(path)
print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(t2)))  # t2 время последнего доступа к файлу
t = os.path.getctime(path)  # время создания файла
print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(t)))

