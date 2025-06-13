# TP7 - Recursividad - Menú de ejercicios

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

def ejer1():
    n = int(input("Ingresá un número entero: "))
    if n < 1:
        print("El número debe ser mayor o igual a 1.")
    else:
        print(f"Factoriales del 1 al {n}:")
        for i in range(1, n + 1):
            print(f"{i}! = {factorial(i)}")

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def ejer2():
    n = int(input("Ingresá hasta qué posición mostrar la serie de Fibonacci: "))
    if n < 0:
        print("La posición debe ser mayor o igual a 0.")
    else:
        print(f"Serie de Fibonacci hasta la posición {n}:")
        for i in range(n + 1):
            print(f"F({i}) = {fibonacci(i)}")

def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)

def ejer3():
    base = int(input("Ingresá la base: "))
    exponente = int(input("Ingresá el exponente: "))
    if exponente < 0:
        print("El exponente debe ser mayor o igual a 0.")
    else:
        resultado = potencia(base, exponente)
        print(f"{base}^{exponente} = {resultado}")

def decimal_a_binario(n):
    if n == 0:
        return ""
    return decimal_a_binario(n // 2) + str(n % 2)

def ejer4():
    n = int(input("Ingresá un número entero positivo: "))
    if n <= 0:
        print("El número debe ser entero positivo.")
    else:
        binario = decimal_a_binario(n)
        print(f"El número {n} en binario es: {binario}")

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

def ejer5():
    palabra = input("Ingresá una palabra (sin espacios ni tildes): ")
    if palabra.isalpha():
        print(f"La palabra '{palabra}' es un palíndromo." if es_palindromo(palabra.lower()) else f"La palabra '{palabra}' no es un palíndromo.")
    else:
        print("Entrada inválida. Usá solo letras.")

def suma_digitos(n):
    if n < 10:
        return n
    return (n % 10) + suma_digitos(n // 10)

def ejer6():
    n = int(input("Ingresá un número entero positivo: "))
    if n <= 0:
        print("El número debe ser entero positivo.")
    else:
        print(f"La suma de los dígitos de {n} es: {suma_digitos(n)}")

def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)

def ejer7():
    n = int(input("Ingresá la cantidad de bloques del nivel más bajo: "))
    if n < 1:
        print("Debe ser un número positivo.")
    else:
        total = contar_bloques(n)
        print(f"Total de bloques necesarios para construir la pirámide: {total}")

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    ultimo = numero % 10
    resto = numero // 10
    if ultimo == digito:
        return 1 + contar_digito(resto, digito)
    else:
        return contar_digito(resto, digito)

def ejer8():
    numero = int(input("Ingresá un número entero positivo: "))
    digito = int(input("Ingresá el dígito que querés contar (0 a 9): "))
    if numero < 0 or digito < 0 or digito > 9:
        print("Datos inválidos. Asegurate de que el número sea positivo y el dígito esté entre 0 y 9.")
    else:
        cantidad = contar_digito(numero, digito)
        print(f"El dígito {digito} aparece {cantidad} veces en {numero}.")

def salir():
    print("¡Hasta luego!")

def menu():
    while True:
        print("\n=== MENÚ TP7 - RECURSIVIDAD ===")
        print("1. Factorial")
        print("2. Fibonacci")
        print("3. Potencia")
        print("4. Decimal a Binario")
        print("5. Palíndromo")
        print("6. Suma de Dígitos")
        print("7. Pirámide de Bloques")
        print("8. Contar Dígito")
        print("0. Salir")
        opcion = input("Elegí una opción: ")

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
        elif opcion == "0":
            salir()
            break
        else:
            print("Opción inválida. Intentá de nuevo.")

if __name__ == "__main__":
    menu()
