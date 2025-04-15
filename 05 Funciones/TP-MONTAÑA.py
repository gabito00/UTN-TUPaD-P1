# Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal.
def imprimir_hola_mundo():
    print("Hola Mundo!")

def ejer1():
    imprimir_hola_mundo()

# Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá 
# devolver: “Hola Marcos!”. Llamar a esta función desde el programa
# principal solicitando el nombre al usuario.
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

def ejer2():
    nombre_usuario = input("Ingrese su nombre: ")
    saludo = saludar_usuario(nombre_usuario)
    print(saludo)

# Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. 
# Pedir los datos al usuario y llamar a esta función con los valores ingresados.
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

def ejer3():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    edad = input("Ingrese su edad: ")
    residencia = input("Ingrese su residencia: ")
    informacion_personal(nombre, apellido, edad, residencia)

# Crear dos funciones: calcular_area_circulo(radio) que reciba el radio 
# como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) 
# que reciba el radio como parámetro y devuelva el perímetro del círculo. 
# Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.
from math import pi

def calcular_area_circulo(radio):
    return pi*radio**2

def calcular_perimetro_circulo(radio):
    return 2*pi*radio

def ejer4():
    radio = float(input("Ingrese el radio: "))
    area = calcular_area_circulo(radio)
    perimetro = calcular_perimetro_circulo(radio)
    print(f"El area del circulo es: {area:.2f} y el perimetro es {perimetro:.2f}")


# Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mostrar
# el resultado usando esta función.
def segundos_a_horas(segundos):
    return segundos / 3600

def ejer5():
    segundos = int(input("Ingrese la cantidad de segundos: "))
    horas = segundos_a_horas(segundos)
    print(f"La conversion de {segundos} segundos a horas es {horas} Hs.")

# Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.
def tabla_multiplicar(numero):
    print(f"La tabla de multiplicar de {numero} es")
    for i in range(1,11):
        print(f"{i} x {numero} = {i*numero}")

def ejer6():
    numero = int(input("Ingrese un numero: "))
    tabla_multiplicar(numero)

# Crear una función llamada operaciones_basicas(a, b) que reciba dos números 
# como parámetros y devuelva una tupla con el resultado de sumarlos,
# restarlos, multiplicarlos y dividirlos.  Mostrar los resultados de forma clara.
def operaciones_basicas(a, b):
    suma = a+b
    resta = a-b
    multiplicacion = a*b
    division = a/b
    return (suma, resta, multiplicacion, division)

def ejer7():
    num1= int(input("Ingrese un numero: "))
    num2= int(input("Ingrese otro numero: "))

    resultados = operaciones_basicas(num1,num2)
    print(f"La resultado de {num1} + {num2} = {resultados[0]}")
    print(f"La resultado de {num1} - {num2} = {resultados[1]}")
    print(f"La resultado de {num1} * {num2} = {resultados[2]}")
    print(f"La resultado de {num1} / {num2} = {resultados[3]}")

# Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la 
# función para mostrar el resultado con dos decimales.
def calcular_imc(peso, altura):
    return peso / (altura**2)

def ejer8():
    altura = float(input("Ingrese su altura en metros: "))
    peso = float(input("Ingrese su peso en KG: "))
    imc = calcular_imc(peso, altura)
    print(f"El IMC es de: {imc:.2f}")

# Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.
def celsius_a_fahrenheit(celsius):
    return celsius * (9 / 5) + 32

def ejer9():
    temp = float(input("Ingrese la temperatura en °C: "))
    print(f"La temperatura de {temp} °C a Fahrenheit es de {celsius_a_fahrenheit(temp)} °F.")

# Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta función.
def calcular_promedio(a, b, c):
    print(f"El promedio es: {(a+b+c)/3}")

def ejer10():
    num1=int(input("Ingrese un numero: "))
    num2=int(input("Ingrese un numero: "))
    num3=int(input("Ingrese un numero: "))
    calcular_promedio(num1, num2, num3)

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