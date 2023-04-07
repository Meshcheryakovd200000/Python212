import json
from random import choice, randint


# Записать словарь словарей в json

def gen_person():
    name = ''
    tel = ''

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    while len(name) != 7:
        name += choice(letters)
    # print(name)

    while len(tel) != 10:
        tel += choice(nums)
    # print(tel)

    person = {
        'name': name,
        'tel': tel
    }
    return person


# print(gen_person())


def write_json(person_dict):  # {'name': 'gadeefa', 'tel': '4193676522'}
    try:
        data = json.load(open('person.json'))  # [{'name': 'gadeefa', 'tel': '4193676522'}]
    except FileNotFoundError:
        data = {}  # если не будет словаря то мы записываем в data пустой словарь

    # data.append(person_dict)  # [{'name': 'gadeefa', 'tel': '4193676522'}, {'name': 'gadeefa', 'tel': '4193676522'}]
    data[randint(144, 9999999997)] = person_dict
    # print(data)
    with open('person.json', 'w') as f:  # f - имя файла
        json.dump(data, f, indent=2)  # отступы 2


for i in range(5):  # 5 словарей
    write_json(gen_person())
