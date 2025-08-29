"""1. Escribir una función llamada saludar(nombre) que reciba un nombre como parámetro e imprima 
un saludo. Luego, el programa debe pedir el nombre del usuario y llamar a la función. 
"""
def saludar(nombre:str):
    print(f"Saludos {nombre}")
    
    
nombre = input("Ingrese su nombre de usuario")
saludar(nombre)