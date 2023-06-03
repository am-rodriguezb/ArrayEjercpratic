import numpy as np
import random 

arreglo = np.random.randint(500, size=(100))
print(arreglo)
arreglo2 = arreglo[:].copy() 
print(arreglo2[99]) # pocision mayor
orden_arreglo = sorted(arreglo2)
print (orden_arreglo[99]) # mayor numero del arreglo
print(orden_arreglo[0]) # menor del arreglo

