S_gl = 0


def fun1_gl(a, b, c):
    global S_gl

    def s_pr(a, b):
        return a * b

    S_gl = 2 * (s_pr(a, c) + s_pr(c, b) + s_pr(a, b))


print("Глобальная переменная")
fun1_gl(2, 4, 6)
print(S_gl)
fun1_gl(5, 8, 2)
print(S_gl)
fun1_gl(1, 6, 8)
print(S_gl)


def fun2_loc(a, b, c):
    def s_pr(a, b):
        return a * b

    s2 = 2 * (s_pr(a, c) + s_pr(c, b) + s_pr(a, b))
    print(s2)


print("\nЛокальная переменная")
fun2_loc(2, 4, 6)
fun2_loc(5, 8, 2)
fun2_loc(1, 6, 8)


def fun3_nonloc(a, b, c):
    s3_nonloc = 0

    def s3(a, b, c):
        nonlocal s3_nonloc

        def s_pr(a, b):
            return a * b

        s3_nonloc = 2 * (s_pr(a, c) + s_pr(c, b) + s_pr(a, b))

    s3(a, b, c)
    print(s3_nonloc)


print("\nНелокальная переменная")
fun3_nonloc(2, 4, 6)
fun3_nonloc(5, 8, 2)
fun3_nonloc(1, 6, 8)
