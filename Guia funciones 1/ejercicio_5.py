"""5. Definir una función es_par(numero) que reciba un número y devuelva True si es par y False si 
es impar. Luego, el programa debe pedir un número y mostrar si es par o impar usando la función. 
"""
def es_par(numero:int) -> bool:
    if numero % 2 == 0:
        retorno = True
    elif numero % 2 == 1:
        retorno = False

    return retorno
numero = int(input("Ingrese un numero: "))
estado = es_par(numero)

if estado:
    print("Es par")
else: 
    print("Es impar")