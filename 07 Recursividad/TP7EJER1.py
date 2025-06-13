def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

n = int(input("Ingresá un número entero: "))
if n < 1:
    print("El número debe ser mayor o igual a 1.")
else:
    print(f"Factoriales del 1 al {n}:")
    for i in range(1, n + 1):
        print(f"{i}! = {factorial(i)}")