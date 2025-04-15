# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).
totalNumero = 0

for i in range(10):
    totalNumero += int(input("Ingrese un numero: "))

print(f"La media es: {totalNumero/10}")