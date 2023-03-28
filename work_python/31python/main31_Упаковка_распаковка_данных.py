# Упаковка данных (серилизация) сохранение данных
# распаковка данных

# marshal (*.рус)
# pickle - модуль
# json

import pickle

# file_name = 'basket.txt'
#
# shop_list = {
#     'фрукты': ['яблоки','манго'],
#     'овощи': 'морковь',
#     'бюджет': 1000
# }
#
# with open(file_name, 'wb') as fh:
#     pickle.dump(shop_list, fh)
#
# with open(file_name, 'rb') as fh:
#     shop_list2 = pickle.load(fh)
# print(shop_list2)

# class Test:
#     num = 35
#     st = 'Привет'
#     lst = [1, 2, 3]
#     d = {'first': 'a', 'second': 2}
#     tpl = (22, 63)
#
#     def __str__(self):
#         return f"Число: {Test.num}\nСтрока: {Test.st}\nСписок: {Test.lst}\nСловарь: {Test.d}\nКортеж: {Test.tpl}"
#
#
# obj = Test()
#
# my_obj = pickle.dumps(obj)
# print(my_obj)
#
# my_obj2 = pickle.loads(my_obj)
# print(my_obj2)

# class Test2:
#     def __init__(self):
#         self.a = 35
#         self.b = 'test'
#         self.c = lambda x: x * x
#
#     def __getstate__(self):
#         attr = self.__dict__.copy()
#         del attr['c']
#         return attr
#
#     def __str__(self):
#         return f"{self.a} {self.b} {self.c(2)}"
#
#     def __setstate__(self, state):
#         self.__dict__ = state
#         self.c = lambda x: x * x
#
#
# item1 = Test2()
# item2 = pickle.dumps(item1)
# item3 = pickle.loads(item2)
# print(item3.__dict__)
# print(item3)
# --------------------------------------------------------

import json
from random import choice


# data = {
#     'name': 'Olga',
#     'age': 35,
#     '20': None,
#     'True': 1,
#     'hobbies': ('running', 'singing'),
#     'children': [
#         {
#             'first_name': 'Alice',
#             'age': 6
#         }
#     ]
# }
#
# with open('data.json', 'w') as fw:
#     json.dump(data, fw, indent=4)  # сдвиг каждого элемента на 4 пробельные символа
#
# with open('data.json', 'r') as fw:
#     data1 = json.load(fw)
# print(data1)
#
# ...
# json_string = json.dumps(data, sort_keys=True)
# print(json_string)  # строка
# print(json_string[10:14])  # строка
#
# data2 = json.loads(json_string)
# print(data2)  # словарь
# print(data2['name'])
# -------------------------------------------

# x = {
#     'name': 'Виктор'
# }
# a = json.dumps(x)
# print(a)
# print(json.loads(a))
#
#
# a = json.dumps(x)
# print(json.dumps(x, ensure_ascii=False))
# -------------------------------------------

# def gen_person():  # &&&&&&&&???????????????????????????????????????????????
#     name = ''
#     tel = ''
#
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
#     nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#
#     while len(name) != 7:
#         name += choice(letters)
#     print(name)
#
#     person = {
#         'name': name,
#         'tel': tel
#     }
#     return person
#
#
# def write_json(person_dict):
#     # список словарей записываем в json объект
#
#     with open('person.json', 'w') as f:
#         json.dump(persons, f, indent=2)
#
#
# # persons = []
# for i in range(5):
#     write_json(gen_person())

# -----------------------------------------------------------------

# zadacha
# class Student
# class Group
# stroka 6780
