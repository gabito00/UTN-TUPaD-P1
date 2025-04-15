# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
# dígitos que contiene. 
numero = int(input("Ingrese un numero entero: "))
digitos = 0
while numero > 0:
    numero = numero // 10
    digitos +=1

print(f"La cantidad de digitos es: {digitos}")