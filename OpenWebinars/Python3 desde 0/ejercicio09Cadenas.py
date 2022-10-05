# Realizar un programa que compruebe si una cadena contiene una subcadena. Las dos cadenas se introducen por teclado.

cadena = str(input("Introduce una cadena: "))
subcadena = str(input("Introduce una subcadena: "))

if(subcadena in cadena):
    print("%s contiene a %s" % (cadena, subcadena))
else:
    print("%s no contiene a %s" % (cadena, subcadena))