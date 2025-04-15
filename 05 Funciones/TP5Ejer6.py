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

if __name__ == "__main__":
    ejer6()