'''2. Sumar todos los elementos: 
Declarar un array de 10 enteros. Cargarlo por teclado. Calcular y mostrar la suma de todos los 
elementos. 
'''
numeros_enteros = [0] * 10
suma_numeros = 0

for i in range(len(numeros_enteros)):
    numeros_enteros[i] = int(input(f"Ingrese el {i + 1}° numero: "))
    suma_numeros += numeros_enteros[i]

print(f"La suma de todos los elementos es: {suma_numeros}")
