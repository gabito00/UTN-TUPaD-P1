def suma_digitos(n):
    if n < 10:
        return n
    return (n % 10) + suma_digitos(n // 10)

n = int(input("Ingresá un número entero positivo: "))
if n <= 0:
    print("El número debe ser entero positivo.")
else:
    print(f"La suma de los dígitos de {n} es: {suma_digitos(n)}")
