# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea. 
def ejer1():
    for i in range(0, 100, 1):
        print(i)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
# dígitos que contiene. 
def ejer2():
    numero = int(input("Ingrese un numero entero: "))
    digitos = 0
    while numero > 0:
        numero = numero // 10
        digitos +=1

    print(f"La cantidad de digitos es: {digitos}")

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
# dados por el usuario, excluyendo esos dos valores. 
def ejer3():
    sumatoria = 0
    inicio = int(input("Ingrese el primero numero: "))
    fin = int(input("Ingrese el segundo numero: "))

    for i in range(inicio+1, fin, 1):
        sumatoria += i
        print(i)

    print(f"La sumatoria es: {sumatoria}")

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en 
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
# un 0. 
def ejer4():
    sumatoria = 0
    numero = int(input("Ingrese un numero: "))
    while numero != 0:
        sumatoria += numero
        numero = int(input("Ingrese un numero: "))

    print(f"La sumatoria es: {sumatoria}")

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
def ejer5():
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

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.
def ejer6():
    for i in range(100,0,-2):
        print(i)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.
def ejer7():
    sumatoria = 0
    numero = int(input("Ingrese un numero: "))

    for i in range(0,numero+1,1):
        sumatoria+=i

    print(f"La sumaoria es: {sumatoria}")

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).
def ejer8():
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

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).
def ejer9():
    totalNumero = 0

    for i in range(100):
        totalNumero += int(input("Ingrese un numero: "))

    print(f"La media es: {totalNumero/100}")

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
def ejer10():
    numero = int(input("Ingrese un numero: "))
    resto = 0
    invertido = 0

    while numero > 0:
        resto = numero%10
        numero=numero//10
        invertido=invertido*10 + resto


    print(invertido)

def salir():
    print("¡Chau capo! 👋")

def menu():
    while True:
        print("\n=== MENÚ ===")
        print("1. Ejercicio 1")
        print("2. Ejercicio 2")
        print("3. Ejercicio 3")
        print("4. Ejercicio 4")
        print("5. Ejercicio 5")
        print("6. Ejercicio 6")
        print("7. Ejercicio 7")
        print("8. Ejercicio 8")
        print("9. Ejercicio 9")
        print("10. Ejercicio 10")
        print("0. Salir")

        opcion = input("Elija una opción: ")

        if opcion == "1":
            ejer1()
        elif opcion == "2":
            ejer2()
        elif opcion == "3":
            ejer3()
        elif opcion == "4":
            ejer4()
        elif opcion == "5":
            ejer5()
        elif opcion == "6":
            ejer6()
        elif opcion == "7":
            ejer7()
        elif opcion == "8":
            ejer8()
        elif opcion == "9":
            ejer9()
        elif opcion == "10":
            ejer10()
        elif opcion == "0":
            salir()
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    menu()