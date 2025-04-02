vocales = "aeiouAEIOU"
frase = input("Ingrese una frase: ")

if frase[-1] in vocales:
    frase += "!"

print(frase)