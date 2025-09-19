'''6. Mayor y su posición: 
Cargar un array de 7 números enteros. Determinar el valor más alto y en qué posición se 
encuentra. 
'''
numeros_enteros = [0] * 7
numero_mayor = 0
bandera = True

for i in range(len(numeros_enteros)):
    numeros_enteros[i] = int(input(f"Ingrese el {i + 1}° numero: "))

for i in range(len(numeros_enteros)):
    if numeros_enteros[i] > numero_mayor or bandera:
        numero_mayor = numeros_enteros[i]
        posicion = i
        bandera = False

print(f"El numero más alto es {numero_mayor} en la posicion {posicion + 1} del vector")
