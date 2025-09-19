'''4. Contar mayores a un valor: 
Cargar un array de 8 enteros. Contar cuántos son mayores al valor 100 e informar el resultado. 
'''
numeros_enteros = [0] * 8
suma_numeros = 0
contador_mayor_a_cien = 0

for i in range(len(numeros_enteros)):
    numeros_enteros[i] = int(input(f"Ingrese el {i + 1}° numero: "))
    suma_numeros += numeros_enteros[i]
    if numeros_enteros[i] > 100:
        contador_mayor_a_cien +=1

print(f"La cantidad de numeros mayores a 100 es: {contador_mayor_a_cien}")