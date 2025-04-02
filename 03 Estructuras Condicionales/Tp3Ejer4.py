edad = int(input("Ingrese su edad: "))

if 0 < edad < 12:
    print("Eres un Niño/a")
elif 12 <= edad < 18:
    print("Eres un Adolescente")
elif 18 <= edad < 30:
    print("Eres un Adulto/a joven")
elif edad >= 30:
    print("Eres un Adulto/a")
else:
    print("Ingresaste una edad errónea")