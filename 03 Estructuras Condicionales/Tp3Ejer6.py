import random
import statistics

numeros_aleatorios = [random.randint(1, 100) for i in range(50)] 
media = statistics.mean(numeros_aleatorios)
mediana = statistics.median(numeros_aleatorios)
moda = statistics.mode(numeros_aleatorios)
#Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la mediana es mayor que la moda. 
# Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez, la mediana es menor que la moda. 
# Sin sesgo: cuando la media, la mediana y la moda son iguales. 
if media > mediana and mediana > moda:
    print("Sesgo positivo.")
elif media < mediana and mediana < moda:
    print("Sesgo negativo.")
elif media == mediana == moda:
    print("Sin sesgo.")
else:
    print("Distribución no claramente sesgada.")
