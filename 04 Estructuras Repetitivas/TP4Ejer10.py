# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
numero = int(input("Ingrese un numero: "))
resto = 0
invertido = 0

while numero > 0:
    resto = numero%10
    numero=numero//10
    invertido=invertido*10 + resto


print(invertido)