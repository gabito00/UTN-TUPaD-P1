# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.
sumatoria = 0
numero = int(input("Ingrese un numero: "))

for i in range(0,numero+1,1):
    sumatoria+=i

print(f"La sumaoria es: {sumatoria}")