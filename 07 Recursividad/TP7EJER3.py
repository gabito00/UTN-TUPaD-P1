def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)

base = int(input("Ingresá la base: "))
exponente = int(input("Ingresá el exponente: "))
if exponente < 0:
    print("El exponente debe ser mayor o igual a 0.")
else:
    resultado = potencia(base, exponente)
    print(f"{base}^{exponente} = {resultado}")
