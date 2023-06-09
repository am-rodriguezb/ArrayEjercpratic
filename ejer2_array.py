import numpy, random

lista= range(1000)
lista_1=random.sample(lista, 10)
lista_1=list(lista_1)
print(lista_1)

for i in range(len(lista_1)):
    if lista_1[i] % 2 ==  0:
        print(lista_1[i])


arreglo_1=numpy.array(lista_1)
valor_max=arreglo_1.max()

for i in range(len(arreglo_1)):
    if arreglo_1[i] == valor_max:
        print(i)