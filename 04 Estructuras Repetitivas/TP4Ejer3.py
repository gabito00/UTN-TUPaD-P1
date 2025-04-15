# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
# dados por el usuario, excluyendo esos dos valores. 
sumatoria = 0
inicio = int(input("Ingrese el primero numero: "))
fin = int(input("Ingrese el segundo numero: "))

for i in range(inicio+1, fin, 1):
    sumatoria += i
    print(i)

print(f"La sumatoria es: {sumatoria}")