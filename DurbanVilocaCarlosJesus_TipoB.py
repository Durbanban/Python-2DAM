

def multar (distancia: int, velocidadPermitida: int, tiempo: int):
    if(tiempo != 0 or velocidadPermitida != 0 or distancia != 0):
        horas = tiempo / 3600
        km = distancia / 1000
        velocidadMediaCoche = km / horas
        diffVelocidades = velocidadMediaCoche / velocidadPermitida
        if(diffVelocidades <= 1 and diffVelocidades > 0):
            return "OK"
        elif(diffVelocidades < 0):
            return "ERROR"
        elif(diffVelocidades > 1 and diffVelocidades < 1.20):
            return "MULTA"
        else:
            return "PUNTOS"
    else:
        return "Ni la velocidad ni el tiempo puede ser 0"

metros = 1
velPermitida = 1
time = 1
filaEntrada = [0, 0, 0]
entrada = []
salida = []

while(metros != 0 and velPermitida != 0 and time != 0):
    metros = int(input("Introduce una distancia (en metros): "))
    velPermitida = int(input("Introduce la velocidad permitida en esta carretera: "))
    time = int(input("Introduce el tiempo que ha tardado en recorrerla (en segundos): "))
    if(metros != 0 and velPermitida != 0):
        salida.append(multar(metros, velPermitida, time))

for mensaje in salida:
    print(mensaje)
