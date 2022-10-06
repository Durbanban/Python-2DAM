# Crea una función “calcularMaxMin” que recibe una lista con valores numéricos y devuelve el valor máximo y el mínimo. Crea un programa que pida números por teclado y muestre el máximo y el mínimo, utilizando la función anterior.

def calcularMaxMin(lista):
    return (max(lista), min(lista))
num = 1
lista = []
while(num != 0):
    num = int(input("Introduce un número (una letra para finalizar el programa): "))
    lista.append(num)

print(calcularMaxMin(lista))