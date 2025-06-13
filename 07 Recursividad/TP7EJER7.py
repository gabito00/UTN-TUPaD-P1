def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)

n = int(input("Ingresá la cantidad de bloques del nivel más bajo: "))

if n < 1:
    print("Debe ser un número positivo.")
else:
    total = contar_bloques(n)
    print(f"Total de bloques necesarios para construir la pirámide: {total}")
