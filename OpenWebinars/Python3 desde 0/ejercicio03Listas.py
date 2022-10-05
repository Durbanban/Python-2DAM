# Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno (comprendidas entre 0 y 10). A continuación 
# debe mostrar todas las notas, la nota media, la nota más alta que ha sacado y la menor.

listaNotas = []
for bucle in range(1, 6):
    nota = int(input("Introduce una nota: "))
    while(nota < 0 or nota > 10):
        print("Error: introduce una nota entre 0 y 10")
        nota = int(input("Introduce una nota: "))
    listaNotas.append(nota)

print("Notas: ", end='')

for bucle in listaNotas:
    print(bucle, '', end='')
print()
print("La nota media es: ", (sum(listaNotas) / len(listaNotas)))
print("La nota máxima es: ", max(listaNotas))
print("La nota mínima es: ", min(listaNotas))