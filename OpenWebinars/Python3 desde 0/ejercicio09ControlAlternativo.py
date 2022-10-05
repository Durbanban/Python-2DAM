# Algoritmo que pida tres números y los muestre ordenados (de mayor a menor)

num1 = int(input("Introduzca el primer número: "))
num2 = int(input("Introduzca el segundo número: "))
num3 = int(input("Introduzca el tercer número: "))

if(num1 > num2 and num1 > num3):
    mayor = num1
    if(num2 > num3):
        mediano = num2
        menor = num3
    else:
        mediano = num3
        menor = num2
elif(num2 > num3 and num2 > num1):
    mayor = num2
    if(num1 > num3):
        mediano = num1
        menor = num3
    else:
        mediano = num3
        menor = num1
elif(num3 > num1 and num3 > num2):
    mayor = num3
    if(num1 > num2):
        mediano = num1
        menor = num2
    else:
        mediano = num2
        menor = num1

print("El número mayor es: ", mayor, ", el mediano es: ", mediano, ", y el menor es: ", menor)