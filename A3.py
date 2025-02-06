def potencia(base, exponente):
    if exponente == 0:
        return 1
    elif exponente < 0:
        return 1 / potencia(base, - exponente)
    else:
        return base * potencia(base, exponente - 1)

print(potencia(2, 3))