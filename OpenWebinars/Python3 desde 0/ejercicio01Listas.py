# Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10) y posteriormente muestre en pantalla
# cada elemento de la lista junto con su cuadrado y su cubo.

import random

lista = []

for bucle in range(1, 11):
    lista.append(random.randint(1, 10))
    
for bucle in lista:
    print(bucle, bucle**2, bucle**3)