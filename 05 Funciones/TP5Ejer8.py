# Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.
def calcular_imc(peso, altura):
    return peso / (altura**2)

def ejer8():
    altura = float(input("Ingrese su altura en metros: "))
    peso = float(input("Ingrese su peso en KG: "))
    imc = calcular_imc(peso, altura)
    print(f"El IMC es de: {imc:.2f}")

if __name__ == "__main__":
    ejer8()