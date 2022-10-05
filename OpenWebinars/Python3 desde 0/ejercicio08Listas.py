# Queremos guardar los nombres y la edades de los alumnos de un curso. Realiza un programa que introduzca el nombre y la edad de cada
# alumno. El proceso de lectura de datos terminará cuando se introduzca como nombre un asterisco (*) Al finalizar se mostrará los
# siguientes datos:

# Todos lo alumnos mayores de edad.
# Los alumnos mayores (los que tienen más edad)

nombre = "placeholder"
edad = 0
listaNombres = []
listaEdades = []

while(nombre != "*"):
    nombre = str(input("Introduce un nombre para el alumno: "))
    if(nombre != "*"):
        edad = int(input("Introduce la edad: "))
        listaNombres.append(nombre)
        listaEdades.append(edad)

print("Mayores de edad")
print("***************")

for nombre, edad in zip(listaNombres, listaEdades):
    if(edad >= 18):
        print(nombre)

print("Alumnos mayores")
print("****************")

for nombre, edad in zip(listaNombres, listaEdades):
    if(edad == max(listaEdades)):
        print(nombre)

