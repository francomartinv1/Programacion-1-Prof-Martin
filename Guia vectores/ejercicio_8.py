'''8. Comparar dos arrays: 
Cargar dos arrays de 5 elementos cada uno. Comparar si ambos son iguales elemento a elemento 
y mostrar un mensaje indicando si son o no iguales. 
'''
numeros_enteros_uno = [0] * 5
numeros_enteros_dos = [0] * 5
bandera = True

print("Array 1:")
for i in range(len(numeros_enteros_uno)):
    numeros_enteros_uno[i] = int(input(f"Ingrese el {i + 1}° numero: "))

print("Array 2:")
for i in range(len(numeros_enteros_dos)):
    numeros_enteros_dos[i] = int(input(f"Ingrese el {i + 1}° numero: "))

for i in range(len(numeros_enteros_uno)):
    if numeros_enteros_uno[i] != numeros_enteros_dos[i]:
        bandera = False

if bandera:
    print("Los numeros de ambos vectores son iguales")
else:
    print("Los numeros de ambos vectores no son iguales")