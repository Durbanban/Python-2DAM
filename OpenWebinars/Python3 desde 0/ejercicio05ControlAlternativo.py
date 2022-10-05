# Escribe un programa que pida un nombre de usuario y una contraseña
# y si se ha introducido "pepe" y "asdasd" se indica "Has entrado al programa"
# sino se da un error.

usuario = str(input("Introduzca nombre de usuario: "))
password = str(input("Introduzca una contraseña: "))

if(usuario != "pepe" or password != "asdasd"):
    print("Error de autentificación")
else:
    print("Acceso permitido")
print("Programa terminado")