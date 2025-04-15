# Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con el resultado de sumarlos,
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

if __name__ == "__main__":
    ejer7()