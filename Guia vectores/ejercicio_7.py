'''7. Invertir orden: 
Cargar un array de 6 enteros y mostrarlo invertido, es decir, desde el último al primero. 
'''
numeros_enteros = [0] * 6
array_invertido = [0] * len(numeros_enteros)
contador = 0


for i in range(len(numeros_enteros)):
    numeros_enteros[i] = int(input(f"Ingrese el {i + 1}° numero: "))

for i in range(len(numeros_enteros)-1,-1,-1):
    array_invertido[contador] = numeros_enteros[i]
    contador +=1

print("Array invertido:")
for i in range(len(array_invertido)):
    print(array_invertido[i])