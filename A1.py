def factorial_it(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

def factorial_rec(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_rec(n - 1)

print(factorial_it(5))
print(factorial_rec(5))