# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la 
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado 
# por pantalla: 
# ● Menor que 3: "Muy leve" (imperceptible). 
# ● Mayor o igual que 3  y menor que 4: "Leve" (ligeramente perceptible). 
# ● Mayor o igual que 4  y menor que 5: "Moderado" (sentido por personas, pero 
# generalmente no causa daños). 
# ● Mayor o igual que 5  y menor que 6: "Fuerte" (puede causar daños en estructuras 
# débiles). 
# ● Mayor o igual que 6  y menor que 7: "Muy Fuerte" (puede causar daños significativos). 
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala). 

magnitud = float(input("Ingrese la magnitud: "))
if 0 < magnitud < 3:
    print("El terremoto fue muy leve.")
elif 3 <= magnitud < 4:
    print("El terremoto fue leve.")
elif 4 <= magnitud < 5:
    print("El terremoto fue moderado.")
elif 5 <= magnitud < 6:
    print("El terremoto fue fuerte.")
elif 6 <= magnitud < 7:
    print("El terremoto fue muy fuerte.")
elif magnitud >= 7:
    print("El terremoto fue extremo.")
else:
    print("La magnitud esta fuera de rango.")