hemisferio = input("Ingrese el hemisferio donde se encuentra Norte(N) o Sur(S): ").strip().upper()
dia = int(input("Ingrese el dia en el que se encuentra (1 - 31): "))
mes = int(input("Ingrese el numero del mes en el que se encuentra (1-12): "))
dias_por_mes = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

if not ((1 <= mes <= 12) and (1 <= dia <= dias_por_mes.get(mes, 0))):
    print("Mes o dia erroneo")
    pass
elif hemisferio == 'N':
    if (mes == 12 and dia >= 21) or (mes == 1 or mes == 2) or (mes == 3 and dia <= 20):
        print("Estas en invierno.")
    elif (mes == 3 and dia >= 21) or (mes == 4 or mes == 5) or (mes == 6 and dia <= 20):
        print("Estas en primavera.")
    elif (mes == 6 and dia >= 21) or (mes == 7 or mes == 8) or (mes == 9 and dia <= 20):
        print("Estas en verano.")
    elif (mes == 9 and dia >= 21) or (mes == 10 or mes == 11) or (mes == 12 and dia <= 20):
        print("Estas en otoño.")
    else:
        print("Dia o mes incorrecto.")
elif hemisferio == 'S':
    if (mes == 12 and dia >= 21) or (mes == 1 or mes == 2) or (mes == 3 and dia <= 20):
        print("Estas en verano.")
    elif (mes == 3 and dia >= 21) or (mes == 4 or mes == 5) or (mes == 6 and dia <= 20):
        print("Estas en otoño.")
    elif (mes == 6 and dia >= 21) or (mes == 7 or mes == 8) or (mes == 9 and dia <= 20):
        print("Estas en invierno.")
    elif (mes == 9 and dia >= 21) or (mes == 10 or mes == 11) or (mes == 12 and dia <= 20):
        print("Estas en primavera.")
    else:
        print("Dia o mes incorrecto.")
else:
    print("Hemisferio incorrecto! las opciones son S o N.")