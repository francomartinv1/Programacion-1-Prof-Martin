'''10. Función para buscar la primera aparición de un valor: 
Escribir una función que reciba un array de enteros y un número a buscar. La función debe retornar 
la posición de la primera aparición de ese número o -1 si no se encuentra. 
'''
def encontrar_primera_aparicion(vector:list, numero_a_buscar:int) -> int:
   posicion = -1
   for i in range(len(vector)):
        if vector[i] == numero_a_buscar:
            posicion = i
            break
   return posicion

numeros_enteros = [0] * 5

for i in range(len(numeros_enteros)):
    numeros_enteros[i] = int(input(f"Ingrese el {i + 1}° numero: "))

numero_a_buscar = int(input("Ingrese un numero que desea encontrar del vector: "))
posicion = encontrar_primera_aparicion(numeros_enteros, numero_a_buscar)

print(posicion)