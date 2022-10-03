import math
cateto1=float(input("Introduce el cateto 1: "))
cateto2=float(input("Introduce el cateto 2: "))
hipotenusa=math.sqrt(math.pow(cateto1, 2)+ math.pow(cateto2, 2))
print("La hipotenusa es: %.2f" % hipotenusa)