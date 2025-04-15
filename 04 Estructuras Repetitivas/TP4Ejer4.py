# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en 
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
# un 0. 

sumatoria = 0
numero = int(input("Ingrese un numero: "))
while numero != 0:
    sumatoria += numero
    numero = int(input("Ingrese un numero: "))

print(f"La sumatoria es: {sumatoria}")

