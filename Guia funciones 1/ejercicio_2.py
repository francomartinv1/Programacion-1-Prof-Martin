"""2. Escribir una función operaciones(num1, num2) que reciba dos números y muestre su suma, 
resta y multiplicación. Luego, el programa debe pedir dos números al usuario y llamar a la 
función. 
"""
def operaciones(num1:float, num2:float):
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    print(f"Suma: {suma}\nResta: {resta}\nMultiplicacion: {multiplicacion}")

num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
operaciones(num1, num2)