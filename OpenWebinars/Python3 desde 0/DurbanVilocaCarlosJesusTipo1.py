# Ejercicio 1

listaMonedas = [5, 2, 1]
listaMonedasUsadas = [0, 0, 0]



cantidadEuros = int(input('Introduzca una cantidad de euros: '))
for moneda in listaMonedas:
    while((cantidadEuros - moneda) >= 0):
        cantidadEuros = cantidadEuros - moneda
        if(moneda == 5):
            listaMonedasUsadas[0] += 1
        elif(moneda == 2):
            listaMonedasUsadas[1] += 1
        else:
            listaMonedasUsadas[2] += 1
    

for moneda, monedaUsada in zip(listaMonedasUsadas, listaMonedas):
    print(moneda, 'monedas de', monedaUsada, 'euros')

