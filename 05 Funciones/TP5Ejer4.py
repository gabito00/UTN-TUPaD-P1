# Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. 
# calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. 
# Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.
from math import pi

def calcular_area_circulo(radio):
    return pi*radio**2

def calcular_perimetro_circulo(radio):
    return 2*pi*radio

def main():
    radio = float(input("Ingrese el radio: "))
    area = calcular_area_circulo(radio)
    perimetro = calcular_perimetro_circulo(radio)
    print(f"El area del circulo es: {area:.2f} y el perimetro es {perimetro:.2f}")


if __name__ == "__main__":
    main()