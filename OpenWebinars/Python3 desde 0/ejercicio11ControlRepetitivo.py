# Escribe un programa que diga si un número introducido por teclado es o no primo. Un número primo es aquel que sólo es divisible entre # él mismo y la unidad. Nota: Es suficiente probar hasta la raíz cuadrada del número para ver si es divisible por algún otro número.

num = int(input("Introduce un número: "))
flag = False
for bucle in range (2, num):
    if(num%bucle==0):
        flag = True
if(flag==True):
    print(num, 'no es primo')
else:
    print(num, 'es primo')