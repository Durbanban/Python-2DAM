# Crea una aplicación que pida un número y calcule su factorial

num = int(input("Introduzca un número: "))

factorial = 2
suma = 1

for bucle in range (1, num, 1):
    suma = suma * factorial
    factorial = factorial + 1

print("El factorial de %d es: %d" % (num, suma))