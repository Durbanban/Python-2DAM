# Escriba un programa que pida una fecha (día, mes y año) y diga si es correcta o no.

dia = int(input("Introduzca un día: "))
mes = int(input("Introduzca un mes: "))
year = int(input("Introduzca un año "))

if(mes in [4, 6, 9, 11]):
    if(dia >= 1 and dia <=30):
        print("Su fecha elegida es: %d / %d / %d" % (dia, mes, year))
    else:
        print("Error: fecha inválida")
elif(mes in [1, 3, 5, 7, 8, 10, 12]):
    if(dia >= 1 and dia <= 31):
        print("Su fecha elegida es: %d / %d / %d" % (dia, mes, year))
    else:
        print("Error: fecha inválida")
elif(mes == 2):
    if(dia >= 1 and dia <= 28):
        print("Su fecha elegida es: %d / %d / %d" % (dia, mes, year))
    else: print("Error: fecha inválida")
else:
    print("Error: fecha inválida")
print("Programa terminado")