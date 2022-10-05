# Algoritmo que pida un número y diga si es positivo, negativo, ó 0.

num = int(input("Introduce un número: "))

if(num>0):
    print(num, "es positivo")
elif(num==0):
    print(num, 'es 0')
else:
    print(num, 'es negativo')
print('Programa terminado')