'''9. Intercambiar elementos pares por ceros: 
Cargar un array de 10 enteros. Reemplazar todos los elementos pares por cero y mostrar el array 
resultante. 
'''
numeros_enteros = [0] * 10

for i in range(len(numeros_enteros)):
    numeros_enteros[i] = int(input(f"Ingrese el {i + 1}° numero: "))

for i in range(len(numeros_enteros)):
    if numeros_enteros[i] % 2 == 0:
        numeros_enteros[i] = 0

for i in range(len(numeros_enteros)):
    print(f"{numeros_enteros[i]}, ",end="")
