'''1. Cargar y mostrar array: 
Declarar un array de 5 enteros. Cargarlo por teclado y mostrar su contenido por pantalla usando un 
ciclo for. 
'''

numeros_enteros = [0] * 5
for i in range(len(numeros_enteros)):
    numeros_enteros[i] = int(input(f"Ingrese el {i + 1}° numero: "))

for i in range(len(numeros_enteros)):
    print(f"Numero {i+1}: {numeros_enteros[i]}")

    









