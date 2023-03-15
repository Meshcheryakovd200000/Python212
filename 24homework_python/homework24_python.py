# Задача 1
# через декоратор @property

class Account:
    rate_usd = 0.013
    rate_eur = 0.011
    sufffix = "RUB"
    sufffix_usd = "USD"
    sufffix_eur = "EUR"

    def __init__(self, surname, num, percent, value=0):
        self.__surname = surname
        self.__num = num  # номер счета
        self.__percent = percent
        self.value = value
        print(f"Счет #{self.__num} принадлежащий {self.__surname} был открыт.")
        print("*" * 50)

    def __del__(self):  # Закрытие счета
        print("*" * 50)
        print(f"Счет #{self.__num} принадлежащий {self.__surname} был закрыт")

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        self.__surname = surname

    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self, num):
        self.__num = num

    @property
    def percent(self):
        return self.__percent

    @percent.setter
    def percent(self, percent):
        self.__percent = percent

    @staticmethod
    def convert(value, rate):
        return value * rate

    @classmethod
    def set_usd_rate(cls, rate):
        cls.rate_usd = rate

    @classmethod
    def set_eur_rate(cls, rate):
        cls.rate_eur = rate

    def print_balance(self):
        print(f"Текущий баланс {self.value} {Account.sufffix}")

    def convert_to_usd(self):
        usd_val = Account.convert(self.value, Account.rate_usd)
        print(f"Состояние счета: {usd_val} {Account.sufffix_usd}")

    def convert_to_eur(self):
        usd_eur = Account.convert(self.value, Account.rate_eur)
        print(f"Состояние счета: {usd_eur} {Account.sufffix_eur}")

    def print_info(self):
        print("Информация о счете:")
        print("-" * 50)
        print(f"#{self.__num}")
        print(f"Владелец: {self.__surname}")
        self.print_balance()
        print(f"Проценты: {self.__percent:.0%}")  # .0% - всё равно что умножим на 100
        print("-" * 50)

    def edit_owner(self, surname):  # смена владельца счета
        self.__surname = surname

    def add_percents(self):
        print("Проценты были успешно начислены")
        self.value += self.value * self.__percent
        print(f"Текущий баланс {self.value} {Account.sufffix}")

    def withdraw(self, val):  # снятие денег со счета
        if val > self.value:
            print(f"К сожалению у вас нет {val} {Account.sufffix}")
        else:
            self.value -= val
            print(f"{val} {Account.sufffix} было успешно снято!")
        self.print_balance()

    def add_money(self, val):  # добавление денег на счет
        self.value += val
        print(f"{val} {Account.sufffix} было успешно добавлено!")
        self.print_balance()


acc = Account(num='12345', surname="Долгих", percent=0.03, value=1000)
# acc.print_balance()
acc.print_info()
acc.convert_to_usd()
acc.convert_to_eur()
print()
Account.set_usd_rate(2)
acc.convert_to_usd()
Account.set_eur_rate(3)
acc.convert_to_eur()
print()
# acc.edit_owner("Дюма")
acc.surname = "Дюма"  # --------------------использовав декоратор @property
acc.num = '98765'  # --------------------использовав декоратор @property
acc.percent = 0.05  # --------------------использовав декоратор @property
acc.print_info()
print()
acc.add_percents()
print()

acc.withdraw(100)
print()
acc.withdraw(3000)
print()
acc.add_money(5000)
print()
acc.withdraw(3000)
print()

# ----------------------

# Задача 2
# через get_...(), set_...()
# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     sufffix = "RUB"
#     sufffix_usd = "USD"
#     sufffix_eur = "EUR"
#
#     def __init__(self, surname, num, percent, value=0):
#         self.__surname = surname
#         self.__num = num  # номер счета
#         self.__percent = percent
#         self.value = value
#         print(f"Счет #{self.__num} принадлежащий {self.__surname} был открыт.")
#         print("*" * 50)
#
#     def __del__(self):  # Закрытие счета
#         print("*" * 50)
#         print(f"Счет #{self.__num} принадлежащий {self.__surname} был закрыт")
#
#     def get_percent(self):
#         return self.__percent
#
#     def set_percent(self, percent):
#         self.__percent = percent
#
#     def get_num(self):
#         return self.__num
#
#     def set_num(self, num):
#         self.__num = num
#
#     def get_surname(self):
#         return self.__surname
#
#     def set_surname(self, surname):
#         self.__surname = surname
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
#         print(f"#{self.__num}")
#         print(f"Владелец: {self.__surname}")
#         self.print_balance()
#         print(f"Проценты: {self.__percent:.0%}")  # .0% - всё равно что умножим на 100
#         print("-" * 50)
#
#     # def edit_owner(self, surname):  # смена владельца счета
#     #     self.__surname = surname
#
#     def add_percents(self):
#         print("Проценты были успешно начислены")
#         self.value += self.value * self.__percent
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
# # acc.edit_owner("Дюма")
# acc.set_surname("Дюма")  # --------------------использовав сеттер
# acc.set_num("987654321")  # --------------------использовав сеттер
# acc.set_percent(0.06)  # --------------------использовав сеттер
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
