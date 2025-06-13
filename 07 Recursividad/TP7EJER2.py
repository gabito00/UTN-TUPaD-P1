def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Ingresá hasta qué posición mostrar la serie de Fibonacci: "))
if n < 0:
    print("La posición debe ser mayor o igual a 0.")
else:
    print(f"Serie de Fibonacci hasta la posición {n}:")
    for i in range(n + 1):
        print(f"F({i}) = {fibonacci(i)}")
