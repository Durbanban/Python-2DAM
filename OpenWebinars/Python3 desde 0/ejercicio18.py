# Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales.

nombre = str(input("Introduzca su nombre: "))
primerApellido = str(input("Introduzca su primer apellido: "))
segundoApellido = str(input("Introduzca su segundo apellido: "))

inicialNombre = nombre[0].upper()
inicialPrimerApellido = primerApellido[0].upper()
incialSegundoApellido = segundoApellido[0].upper()

print("Sus iniciales son: ", inicialNombre,'.', inicialPrimerApellido,'.', incialSegundoApellido)