# Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.
def celsius_a_fahrenheit(celsius):
    return celsius * (9 / 5) + 32

def ejer9():
    temp = float(input("Ingrese la temperatura en °C: "))
    print(f"La temperatura de {temp} °C a Fahrenheit es de {celsius_a_fahrenheit(temp)} °F.")

if __name__ == "__main__":
    ejer9()
