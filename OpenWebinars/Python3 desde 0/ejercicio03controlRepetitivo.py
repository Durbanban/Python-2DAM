# Algoritmo que pida números hasta que introduzca un cero. Debemos imprimir
# la suma y la media de todos los números introducidos.

num = int(input("Introduzca un número: "))
cont = 0
suma = 0
while (num != 0):
    suma = suma + num
    cont+=1
    num = int(input("Introduzca otro número: "))
if(cont > 0):
    media = suma / cont
else: 
    media = 0
print(suma, (media))