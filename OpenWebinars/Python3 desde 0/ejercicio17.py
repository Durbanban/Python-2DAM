# Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos.
# El tiempo de viaje hasta llegar a otra ciudad B es de T segundos.
# Escribir un algoritmo que determine la hora de llegada de la ciudad B.

horas = int(input("¿Qué hora era cuando salió?: "))
minutos = int(input("¿Qué minuto era cuando salió?"))
segundos = int(input("¿Qué segundo era cuando salió?"))

viaje = int(input("¿Cuántos segundos ha tardado?"))

horaInicialSec = (horas * 3600) + (minutos * 60) + (segundos)

horaInicialSec = horaInicialSec + viaje

horas = horaInicialSec//3600
minutos = (horaInicialSec%3600) //60
segundos = (horaInicialSec%3600) % 60

print('El ciclista llegó a las ', horas, 'HH', minutos, 'MM', segundos, 'SS')

