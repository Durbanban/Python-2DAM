# Un alumno desea saber cual será su calificaciópn final en la materia
# Dicha calificación se compone de los siguientes porcentajes:
# * 55% del promedio de sus tres calificaciones parciales
# * 30% de la calificación del examen final
# * 15% de la calificación de un trabajo final 

primerParcial=float(input("Introduzca la primera nota parcial: "))
segundoParcial=float(input("Introduzca la segunda nota parcial: "))
tercerParcial=float(input("Introduzca la tercera nota parcial: "))

examenFinal=float(input("Introduzca la nota del examen final: "))

trabajoFinal=float(input("Introduzca la nota del trabajo final: "))

promedioParciales=(primerParcial+segundoParcial+tercerParcial) / 3

notaFinal=((promedioParciales*0.55)+(examenFinal*0.30)+(trabajoFinal*0.15))

print("Su nota final es: %.2f" % notaFinal)