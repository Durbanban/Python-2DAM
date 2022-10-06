# Crea un programa que pida dos números enteros al usuario y diga si alguno de ellos es múltiplo del otro. Crea una función EsMultiplo que reciba los dos números, y devuelve si el primero es múltiplo del segundo.

num1 = int(input("Introduzca el primer número: "))
num2 = int(input("Introduzca el segundo número: "))

def esMultiplo(a, b):
    resultado = ''
    if(a % b != 0):
        resultado = "No es múltiplo"
    else:
        resultado = "Es múltiplo"
    return resultado

print(esMultiplo(num1, num2))    