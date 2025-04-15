# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
import random

nroRandom = random.randint(0, 9)
control = False
numero = int(input("Ingrese un numero entre 0 y 9: "))

while not control:
    if numero == control:
        print("Bien! adivinaste.")
        control = True
    else:
        print("Que mal, no lograste adivinar, segui intentando.")
        numero = int(input("Ingrese un numero entre 0 y 9: "))
