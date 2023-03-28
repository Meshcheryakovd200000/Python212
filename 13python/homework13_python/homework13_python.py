def args_decorator(fn):
    def wrap(*args):
        print("Среднее арифметическое чисел", str(args)[1:-1], "=", fn(*args) / len(args))
    return wrap


@args_decorator
def summa(*args):

    print("Сумма чисел", str(args)[1:-1], "=", sum(args))
    return sum(args)


summa(2, 3, 3, 4)
