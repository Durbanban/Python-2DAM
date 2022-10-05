#Pide una cadena y un carácter por teclado (valida que sea un carácter) y muestra cuantas veces aparece el carácter en la cadena.

cadena = str(input("Introduce una cadena: "))
caracter = str(input("Introduce un carácter:"))

while (len(caracter) != 1):
    print("Error: el carácter no puede ser más de 1 pulsación")
    caracter = str(input("Introduce un carácter: "))

print(cadena.count(caracter))
