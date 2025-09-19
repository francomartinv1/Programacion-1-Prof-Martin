'''3. Promedio de valores: 
Declarar un array de 6 números reales (floats). Cargarlo por teclado. Calcular y mostrar el promedio 
de los valores. 
'''
numeros_flotantes = [0.0] * 6
suma_numeros = 0

for i in range(len(numeros_flotantes)):
    numeros_flotantes[i] = float(input(f"Ingrese el {i + 1}° numero: "))
    suma_numeros += numeros_flotantes[i]

promedio = suma_numeros / len(numeros_flotantes)
print(f"El promedio de los valores es: {promedio}")


