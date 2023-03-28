# video 47 пара

# class Date:
#     def __init__(self, day, month, year):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     @classmethod
#     def from_string(cls, date_as_string):
#         day, month, year = map(int, date_as_string.split("."))
#         return cls(day, month, year)
#
#     @staticmethod
#     def is_date_valid(date_as_string):
#         if date_as_string.count(".") == 2:
#             day, month, year = map(int, date_as_string.split("."))
#             return day <= 31 and month <= 12 and year <= 3999
#
#     def string_to_db(self):
#         return f"{self.year}-{self.month}-{self.day}"
#
#
# dates = [
#     '30.12.2020',
#     '30-12-2020',
#     '89.12.2021',
#     '12.45.2022'
# ]
#
# for string_date in dates:
#     if Date.is_date_valid(string_date):
#         date = Date.from_string(string_date)
#         string_to_db = date.string_to_db()
#         print(string_to_db)
#     else:
#         print("Неправильная дата или формат строки с датой")
#
#
# string_date = "23.10.2021"
# day, month, year = map(int, string_date.split("."))
# date = Date(day, month, year)
# date = Date.from_string("23.10.2021")  # date = Date(23, 10, 2021)
# print(date.string_to_db())
#
#
# string_date2 = "15.11.2022"
# day, month, year = map(int, string_date2.split("."))
# date2 = Date.from_string("15.11.2022")
# print(date2.string_to_db())

# ----------------------------------------------------------------------
# video 47
# Задача

# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     sufffix = "RUB"
#     sufffix_usd = "USD"
#     sufffix_eur = "EUR"
#
#     def __init__(self, surname, num, percent, value=0):
#         self.surname = surname
#         self.num = num  # номер счета
#         self.percent = percent
#         self.value = value
#         print(f"Счет #{self.num} принадлежащий {self.surname} был открыт.")
#         print("*" * 50)
#
#     def __del__(self):  # Закрытие счета
#         print("*" * 50)
#         print(f"Счет #{self.num} принадлежащий {self.surname} был закрыт")
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
#
#     def print_balance(self):
#         print(f"Текущий баланс {self.value} {Account.sufffix}")
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.value, Account.rate_usd)
#         print(f"Состояние счета: {usd_val} {Account.sufffix_usd}")
#
#     def convert_to_eur(self):
#         usd_eur = Account.convert(self.value, Account.rate_eur)
#         print(f"Состояние счета: {usd_eur} {Account.sufffix_eur}")
#
#     def print_info(self):
#         print("Информация о счете:")
#         print("-" * 50)
#         print(f"#{self.num}")
#         print(f"Владелец: {self.surname}")
#         self.print_balance()
#         print(f"Проценты: {self.percent:.0%}")  # .0% - всё равно что умножим на 100
#         print("-" * 50)
#
#     def edit_owner(self, surname):  # смена владельца счета
#         self.surname = surname
#
#     def add_percents(self):
#         print("Проценты были успешно начислены")
#         self.value += self.value * self.percent
#         print(f"Текущий баланс {self.value} {Account.sufffix}")
#
#     def withdraw(self, val):  # снятие денег со счета
#         if val > self.value:
#             print(f"К сожалению у вас нет {val} {Account.sufffix}")
#         else:
#             self.value -= val
#             print(f"{val} {Account.sufffix} было успешно снято!")
#         self.print_balance()
#
#     def add_money(self, val):  # добавление денег на счет
#         self.value += val
#         print(f"{val} {Account.sufffix} было успешно добавлено!")
#         self.print_balance()
#
#
# acc = Account(num='12345', surname="Долгих", percent=0.03, value=1000)
# # acc.print_balance()
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
# Account.set_usd_rate(2)
# acc.convert_to_usd()
# Account.set_eur_rate(3)
# acc.convert_to_eur()
# print()
# acc.edit_owner("Дюма")
# acc.print_info()
# print()
# acc.add_percents()
# print()
#
# acc.withdraw(100)
# print()
# acc.withdraw(3000)
# print()
# acc.add_money(5000)
# print()
# acc.withdraw(3000)
# print()

# ----------------------------------------------

import re


class UserDate:  # и в main25 продолжение разбирать
    def __init__(self, fio, old, ps, weight):
        self.verify_fio(fio)
        self.verify_old(old)
        self.verify_weight(weight)
        self.verify_ps(ps)

        self.fio = fio
        self.old = old
        self.password = ps
        self.weight = weight

    @staticmethod
    def verify_fio(fio):
        if not isinstance(fio, str):
            raise TypeError("ФИО должно быть строкой")
        f = fio.split()  # ['Волков', 'Игорь', 'Николаевич']
        # print(f)
        if len(f) != 3:
            raise TypeError("Неверный формат ФИО")
        # ['В', 'о', 'л', 'к', 'о', 'в', 'И', 'г', 'о', 'р', 'ь', 'Н', 'и', 'к', 'о', 'л', 'а', 'е', 'в', 'и', 'ч']
        letters = "".join(re.findall(r'[а-яё-]', fio, re.IGNORECASE))  # ВолковИгорьНиколаевич
        # print(letters)
        for s in f:
            # print(s.strip(letters))
            if len(s.strip(letters)) != 0:
                raise TypeError("В ФИО можно использовать только буквы и дефис")


#     @staticmethod
#     def verify_old(old):
#         if not isinstance(old, int) or old < 18 or old > 90:
#             raise TypeError("Возраст должен быть числом в диапазоне от 18 до 90 лет")
#
#     @staticmethod
#     def verify_weight(w):
#         if not isinstance(w, float) or w < 20:
#             raise TypeError("Вес должен быть вещественным числом от 20 кг и выше")
#
#     @staticmethod
#     def verify_ps(ps):
#         if not isinstance(ps, str):
#             raise TypeError("Паспорт должен быть строкой")
#         s = ps.split()  # ['1234', '567890']
#         if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
#             raise TypeError("Неверный формат паспорта")
#         for p in s:
#             if not p.isdigit():
#                 raise TypeError("Серия и номер паспорта должны быть числами")
#
#     @property
#     def fio(self):
#         return self.__fio
#
#     @fio.setter
#     def fio(self, fio):
#         self.verify_fio(fio)
#         self.__fio = fio
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, year):
#         self.verify_old(year)
#         self.__old = year
#
#     @property
#     def weight(self):
#         return self.__weight
#
#     @weight.setter
#     def weight(self, w):
#         self.verify_weight(w)
#         self.__weight = w
#
#     @property
#     def password(self):
#         return self.__password
#
#     @password.setter
#     def password(self, ps):
#         self.verify_ps(ps)
#         self.__password = ps
#
#
p1 = UserDate("Волков Игорь Николаевич", 26, '1234 567890', 80.8)
# p1.fio = "Соболев Игорь Николаевич"
# p1.old = 35
# p1.password = '4567 123456'
# p1.weight = 70.0
# print(p1.__dict__)
