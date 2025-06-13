def contar_digito(numero, digito):
    if numero == 0:
        return 0
    ultimo = numero % 10
    resto = numero // 10
    if ultimo == digito:
        return 1 + contar_digito(resto, digito)
    else:
        return contar_digito(resto, digito)


numero = int(input("Ingresá un número entero positivo: "))
digito = int(input("Ingresá el dígito que querés contar (0 a 9): "))

if numero < 0 or digito < 0 or digito > 9:
    print("Datos invalidos. Asegurate de que el número sea positivo y el dígito esté entre 0 y 9.")
else:
    cantidad = contar_digito(numero, digito)
    print(f"El dígito {digito} aparece {cantidad} veces en {numero}.")
