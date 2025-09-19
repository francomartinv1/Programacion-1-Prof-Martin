'''5. Buscar un valor: 
Cargar un array de 10 enteros. Solicitar al usuario un número y verificar si se encuentra en el array. 
Informar la posición en caso afirmativo, o indicar que no se encuentra. 
'''
numeros_enteros = [1, 5, 2, 10, 7, 11, 4, 9, 25, 30]
encontro_valor = False
numero_elegido = int(input("Ingrese un numero para verificar si esta en el array: "))

for i in range(len(numeros_enteros)):
    if numeros_enteros[i] == numero_elegido:
        posicion = i
        encontro_valor = True

if encontro_valor:
    print(f"Se encontro un valor en la posicion {posicion + 1} del array")
else:
    print("No se encontro el valor en el array")
