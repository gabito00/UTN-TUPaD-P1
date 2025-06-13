def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

palabra = input("Ingresá una palabra (sin espacios ni tildes): ")

if palabra.isalpha():
    print(f"La palabra '{palabra}' es un palíndromo." if es_palindromo(palabra.lower()) else f"La palabra '{palabra}' no es un palíndromo.")
else:
    print("Entrada inválida. Usá solo letras.")
