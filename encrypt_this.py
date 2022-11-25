

ejemplo = str(input("Indica un mensaje a cifrar"))


def encriptar(texto):
    palabras = texto.split(" ")
    resultado = []
    for palabra in palabras:
        letraNueva = ""
        letraAux = ""
        for posLetra in range(len(palabra)):
            if posLetra == 0:
                letraNueva += str(ord(palabra[posLetra]))
            elif posLetra == 1:
                letraAux = palabra[posLetra]
                letraNueva += palabra[-1]
            elif posLetra == len(palabra) - 1:
                letraNueva += letraAux
            else:
                letraNueva += palabra[posLetra]
        resultado.append(letraNueva)
    return " ".join(list(filter(None, resultado)))


print("Tu mensaje era: ", ejemplo, "\nY ahora es: ", encriptar(ejemplo))
