# Suponiendo que hemos introducido una cadena por teclado que representa una frase (palabras separadas por espacios), realiza un
# programa que cuente cuantas palabras tiene.

cadena = str(input("Introduzca una cadena: "))
cont = 1

cadena = cadena.strip()

for bucle in cadena:
    if(bucle==' '):
        cont+=1
print("La frase tiene %d palabras" % cont)
