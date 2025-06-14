def ejer1():
    precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melon': 3000, 'Uva': 1450}
    precios_frutas['Naranja'] = 1200
    precios_frutas['Manzana'] = 1500
    precios_frutas['Pera'] = 2300
    print("Después de añadir frutas:", precios_frutas)
    return precios_frutas

def ejer2():
    precios_frutas = ejer1()
    precios_frutas['Banana'] = 1330
    precios_frutas['Manzana'] = 1700
    precios_frutas['Melon'] = 2800
    print("Diccionario final de precios:", precios_frutas)
    return precios_frutas

def ejer3():
    precios_frutas = ejer2()
    lista_frutas = list(precios_frutas.keys())
    print("Lista de frutas (solo nombres):", lista_frutas)
    return lista_frutas



def ejer4():
    contactos = {}
    print("Ingrese 5 contactos (nombre y número).")
    for i in range(5):
        nombre = input(f"Contacto {i+1} - Nombre: ").strip()
        numero = input(f"Contacto {i+1} - Número: ").strip()
        contactos[nombre] = numero
    print("Contactos guardados.")
    consulta = input("Ingrese un nombre para consultar número: ").strip()
    if consulta in contactos:
        print(f"Número de {consulta}: {contactos[consulta]}")
    else:
        print(f"No existe un contacto con nombre '{consulta}'.")

def ejer5():
    frase = input("Ingrese una frase: ").strip()
    palabras = frase.split()
    únicas = set(palabras)
    print("Palabras únicas:", únicas)
    conteo = {}
    for palabra in palabras:
        conteo[palabra] = conteo.get(palabra, 0) + 1
    print("Conteo de apariciones:", conteo)

def ejer6():
    alumnos = {}
    for i in range(3):
        nombre = input(f"Ingrese nombre del alumno {i+1}: ").strip()
        notas_str = input(f"Ingrese 3 notas de {nombre}, separadas por espacios: ").strip()
        try:
            notas = tuple(float(x) for x in notas_str.split())
            if len(notas) != 3:
                print("Debe ingresar exactamente 3 notas. Se intenta de nuevo.")
                return
            alumnos[nombre] = notas
        except ValueError:
            print("Notas inválidas. Use números separados por espacios.")
            return
    for nombre, notas in alumnos.items():
        promedio = sum(notas) / len(notas)
        print(f"Promedio de {nombre}: {promedio:.2f}")

def ejer7():
    aprobados_parcial1 = {201, 202, 203, 204, 205, 206}
    aprobados_parcial2 = {204, 205, 207, 208, 209}

    print("Aprobados Parcial 1:", aprobados_parcial1)
    print("Aprobados Parcial 2:", aprobados_parcial2)

    aprobados_ambos = aprobados_parcial1 & aprobados_parcial2
    aprobados_solo_uno = aprobados_parcial1.symmetric_difference(aprobados_parcial2)
    aprobados_al_menos_uno = aprobados_parcial1 | aprobados_parcial2

    print("\nResultados usando sets:")
    print(" - Aprobados en ambos parciales:", aprobados_ambos)
    print(" - Aprobados solo en uno de los dos parciales:", aprobados_solo_uno)
    print(" - Aprobados en al menos un parcial:", aprobados_al_menos_uno)

    print("\nResultados ordenados:")
    print(" - Aprobados en ambos parciales (ordenados):", sorted(aprobados_ambos))
    print(" - Aprobados solo en uno de los dos parciales (ordenados):", sorted(aprobados_solo_uno))
    print(" - Aprobados en al menos un parcial (ordenados):", sorted(aprobados_al_menos_uno))


def ejer8():
    stock = {}
    accion = ''
    while accion != 'salir':
        accion = input("Seleccione acción: [consultar, agregar_unidades, nuevo, salir]: ").strip().lower()
        if accion == 'consultar':
            prod = input("Ingrese nombre de producto: ").strip()
            if prod in stock:
                print(f"Stock de {prod}: {stock[prod]}")
            else:
                print(f"Producto '{prod}' no existe.")
        elif accion == 'agregar_unidades':
            prod = input("Ingrese nombre de producto existente: ").strip()
            if prod in stock:
                unidades = int(input("Ingrese unidades a agregar: ").strip())
                stock[prod] += unidades
                print(f"Nuevo stock de {prod}: {stock[prod]}")
            else:
                print(f"Producto '{prod}' no existe.")
        elif accion == 'nuevo':
            prod = input("Ingrese nombre de nuevo producto: ").strip()
            if prod not in stock:
                unidades = int(input("Ingrese stock inicial: ").strip())
                stock[prod] = unidades
                print(f"Producto '{prod}' agregado con stock {unidades}.")
            else:
                print("El producto ya existe. Use 'agregar_unidades' para sumar stock si lo desea.")
        elif accion == 'salir':
            break
        else:
            print("Acción no reconocida. Use 'consultar', 'agregar_unidades', 'nuevo' o 'salir'.")
    print("Saliendo de gestión de stock.")


def ejer9():
    agenda = {}
    print("Para ingresar eventos, use formato 'día,hora' (ejemplo: Lunes,14:00). Escriba 'fin' para terminar.")
    while True:
        entrada = input("Ingrese día y hora o 'fin' para terminar: ").strip()
        if entrada.lower() == 'fin':
            break
        if ',' in entrada:
            partes = [x.strip() for x in entrada.split(',', 1)]
            if len(partes) == 2 and partes[0] and partes[1]:
                dia, hora = partes
                evento = input("Descripción del evento: ").strip()
                agenda[(dia, hora)] = evento
                print(f"Evento agregado: {dia} a las {hora} → {evento}")
            else:
                print("Formato incorrecto: debe ser 'día,hora' con ambas partes no vacías.")
        else:
            print("Formato incorrecto: use 'día,hora' con una coma separadora.")

    consulta = input("Ingrese día y hora a consultar (ejemplo: Lunes,14:00): ").strip()
    if ',' in consulta:
        partes = [x.strip() for x in consulta.split(',', 1)]
        if len(partes) == 2 and partes[0] and partes[1]:
            dia, hora = partes
            clave = (dia, hora)
            if clave in agenda:
                print(f"Evento en {dia} a las {hora}: {agenda[clave]}")
            else:
                print(f"No hay evento para {dia} a las {hora}.")
        else:
            print("Formato de consulta incorrecto: debe ser 'día,hora' con ambas partes no vacías.")
    else:
        print("Formato de consulta incorrecto: use 'día,hora' con una coma separadora.")

    if agenda:
        print("\nAgenda completa:")
        for (d, h), ev in agenda.items():
            print(f" - {d} a las {h}: {ev}")
    else:
        print("La agenda quedó vacía.")


def ejer10():
    pais_capital = {}
    print("Ingrese pares país-capital. Para terminar, ingrese 'fin' como país.")
    while True:
        pais = input("País: ").strip()
        if pais.lower() == 'fin':
            break
        capital = input("Capital: ").strip()
        pais_capital[pais] = capital
    inverso = {capital: pais for pais, capital in pais_capital.items()}
    print("Diccionario invertido (capital -> país):", inverso)

def menu():
    opciones = {
        '1': ("Ejer 1", ejer1),
        '2': ("Ejer 2", ejer2),
        '3': ("Ejer 3", ejer3),
        '4': ("Ejer 4", ejer4),
        '5': ("Ejer 5", ejer5),
        '6': ("Ejer 6", ejer6),
        '7': ("Ejer 7", ejer7),
        '8': ("Ejer 8", ejer8),
        '9': ("Ejer 9", ejer9),
        '10': ("Ejer 10" , ejer10),
        '11': ("Salir", None)
    }
    while True:
        print("\nSeleccione ejercicio:")
        for key, (desc, _) in opciones.items():
            print(f"{key}. {desc}")
        elec = input("Elección: ").strip()
        if elec == '11':
            print("Saliendo.")
            break
        if elec in opciones:
            func = opciones[elec][1]
            if func:
                func()
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()
