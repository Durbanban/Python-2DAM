# Escribe un programa que lea una cadena y devuelva un diccionario con la cantidad de apariciones de cada carácter en la cadena.

dict = {}
cadena = str(input("Introduzca una cadena: "))

for caracter in cadena:
    dict[caracter] = cadena.count(caracter)

for clave, valor in dict.items():
    print(clave, '->', valor)


