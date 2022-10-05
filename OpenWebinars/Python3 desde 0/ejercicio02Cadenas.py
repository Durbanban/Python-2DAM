#Realizar un programa que comprueba si una cadena leída por teclado comienza por una subcadena introducida por teclado.

cadena = str(input("Introduzca una cadena: "))
subCadena = str(input("Introduzca una cadena para comprobar si comienza por esta: "))

if(cadena.startswith(subCadena)):
    print("Sí, comienza por esa cadena")
else:
    print("No, no comienza por esa cadena")
