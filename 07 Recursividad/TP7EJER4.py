def decimal_a_binario(n):
    if n == 0:
        return ""
    return decimal_a_binario(n // 2) + str(n % 2)

n = int(input("Ingresá un número entero positivo: "))
if n <= 0:
    print("El número debe ser entero positivo.")
else:
    binario = decimal_a_binario(n)
    print(f"El número {n} en binario es: {binario}")
