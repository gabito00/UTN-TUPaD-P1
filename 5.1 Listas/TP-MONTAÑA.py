def ejer1():
    # 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función
    # range.
    miLista = list(range(4,101,4))
    print(miLista)

def ejer2():
    # 2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el
    # penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el
    # indexing con números negativos!
    miLista = ["Hola", "Buen Dia", "Buenas Tardes", "Buenas Noches", "Adios"]
    print(miLista[-2])
    
def ejer3():
    # 3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por
    # pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por
    # ejemplo:
    # lista_vacia = []
    nombreCompleto = []
    nombreCompleto.append("Gabriel")
    nombreCompleto.append("Maximiliano")
    nombreCompleto.append("Montaña")
    print(nombreCompleto)

def ejer4():
    # 4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
    # respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra
    # en los videos o bien investigar cómo funciona el indexing con números negativos!
    # animales = ["perro", "gato", "conejo", "pez"]

    animales = ["perro", "gato", "conejo", "pez"]
    animales[0]="loro"
    animales[-1]="oso"
    print(animales)

def ejer5():
    # 5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
    # numeros = [0, 15, 3, 22, 7]
    # numeros.remove(max(numeros))
    # print(numeros)
    primerPaso= "Crea una lista con los numeros 0, 15, 3, 22 y 7"
    segundoPaso = "Identifica el maximo numero en la lista"
    tercerPaso = "Elimina el maximo valor de la lista con la funcion remove, en este caso seria numeros.remove(22)"
    print(primerPaso + "\n" + segundoPaso + "\n" + tercerPaso)

def ejer6():
    # 6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por
    # pantalla los dos primeros.
    myList = list(range(10,31,5))
    print(myList[0:2]) 

def ejer7():
    # 7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores
    # cualesquiera.

    autos = ["sedan", "polo", "suran", "gol"]

    autos[1]="Golf"
    autos[2]="T-Cross"
    print(autos)

def ejer8():
    # 8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append
    # directamente. Imprimir la lista resultante por pantalla.

    dobles = []
    dobles.append(5*2)
    dobles.append(10*2)
    dobles.append(15*2)
    print(dobles)

def ejer9():
    # 9) Dada la lista “compras”, cuyos elementos representan los productos comprados por
    # diferentes clientes:
    # compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
    # a) Agregar "jugo" a la lista del tercer cliente usando append.
    # b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
    # c) Eliminar "pan" de la lista del primer cliente.
    # d) Imprimir la lista resultante por pantalla
    compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
    #######
    ## a ##
    #######
    compras[2].append("jugo")

    #######
    ## b ##
    #######
    compras[1][1] = "tallarines"

    #######
    ## c ##
    #######
    compras[0].remove("pan")

    #######
    ## d ##
    #######
    print(compras)

def ejer10():
    # 10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
    # ● Posición lista_anidada[0]: 15
    # ● Posición lista_anidada[1]: True
    # ● Posición lista_anidada[2][0]: 25.5
    # ● Posición lista_anidada[2][1]: 57.9
    # ● Posición lista_anidada[2][2]: 30.6
    # ● Posición lista_anidada[3]: False
    # Imprimir la lista resultante por pantalla.
    lista_anidada = [15, True, [25.5, 57.9, 30.6], False]

    print(lista_anidada)



def salir():
    print("¡Chau capo! 👋")

def menu():
    while True:
        print("\n=== MENÚ ===")
        print("1. Ejercicio 1")
        print("2. Ejercicio 2")
        print("3. Ejercicio 3")
        print("4. Ejercicio 4")
        print("5. Ejercicio 5")
        print("6. Ejercicio 6")
        print("7. Ejercicio 7")
        print("8. Ejercicio 8")
        print("9. Ejercicio 9")
        print("10. Ejercicio 10")
        print("0. Salir")

        opcion = input("Elija una opción: ")

        if opcion == "1":
            ejer1()
        elif opcion == "2":
            ejer2()
        elif opcion == "3":
            ejer3()
        elif opcion == "4":
            ejer4()
        elif opcion == "5":
            ejer5()
        elif opcion == "6":
            ejer6()
        elif opcion == "7":
            ejer7()
        elif opcion == "8":
            ejer8()
        elif opcion == "9":
            ejer9()
        elif opcion == "10":
            ejer10()
        elif opcion == "0":
            salir()
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    menu()