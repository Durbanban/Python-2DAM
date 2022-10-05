# Realizar un algoritmo que muestre la tabla de multiplicar de un número
# introducido por teclado.

num = int(input("Introduzca un número: "))

for bucle in range(1, 11):
    print(num, 'X', bucle, '=', (num*bucle))