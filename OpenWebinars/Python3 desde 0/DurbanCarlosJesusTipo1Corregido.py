# Ejercicio 1 Corregido

listaMonedas = [5, 2, 1]
listaMonedasUsadas = [0, 0, 0]
i = 0



cantidadEuros = int(input('Introduzca una cantidad de euros: '))
for moneda in listaMonedas:
    while(cantidadEuros >= moneda):
        cantidadEuros = cantidadEuros - moneda
        listaMonedasUsadas[i] += 1
    i+=1

for moneda, monedaUsada in zip(listaMonedasUsadas, listaMonedas):
    print(moneda, 'monedas de', monedaUsada, 'euros')