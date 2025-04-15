# Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función.
def calcular_promedio(a, b, c):
    print(f"El promedio es: {(a+b+c)/3}")

def ejer10():
    num1=int(input("Ingrese un numero: "))
    num2=int(input("Ingrese un numero: "))
    num3=int(input("Ingrese un numero: "))
    calcular_promedio(num1, num2, num3)

if __name__ == "__main__":
    ejer10()