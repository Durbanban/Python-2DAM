

def multar (distancia: int, velocidadPermitida: int, tiempo: int):
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

metros = 1
velPermitida = 1
time = 1
filaEntrada = [0, 0, 0]
entrada = []

while(metros != 0 and velPermitida != 0 and time != 0):
    metros = int(input("Introduce una distancia (en metros): "))
    velPermitida = int(input("Introduce la velocidad permitida en esta carretera: "))
    time = int(input("Introduce el tiempo que ha tardado en recorrerla (en segundos): "))
    filaEntrada[0] = metros
    filaEntrada[1] = velPermitida
    filaEntrada[2] = time
    if(filaEntrada[0] != 0 and filaEntrada[1] != 0 and filaEntrada[2] != 0):
        entrada.append(filaEntrada)

print("Me ha faltado asignar las variables de entrada a cada una de las filas. El método multar es funcional")
