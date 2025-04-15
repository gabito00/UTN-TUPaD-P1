# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).
pares=0
impares=0
positivos=0
negativos=0

for i in range(1,101):
    numero = int(input("Ingrese un numero: "))
    if numero > 0:
        positivos +=1
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
    else:
        negativos += 1
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1

print(f"La cantidad de pares es: {pares}, impares es: {impares}, positivos es: {positivos} y negativos es: {negativos}")
