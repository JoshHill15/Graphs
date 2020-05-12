def f(n):
    if n == 0:
        return 2
    else:
        return f(n-1) * 2


print(f(3))
