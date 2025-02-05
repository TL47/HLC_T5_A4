def suma(n):
    if n == 0:
        return 0
    return n%10 + suma(int(n/10))

print(suma(1234))