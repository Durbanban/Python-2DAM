# Dadas dos variables numéricas A y B, que el usuario debe teclear,
# se pide realizar un algoritmo intercambiable que intercambie los valores de ambas
# y muestre cuánto valen al final las dos variables

a=int(input("Introduzca la primera variable: "))
b=int(input("Introduzca la segunda variable: "))
print("La variable A es: ",a, "y la variable B es: ",b)
aux=a
a=b
b=aux

print("La variable A es: ", a, "y la variable B es: ",b)