"""1. Escribir una función llamada saludar(nombre) que reciba un nombre como parámetro e imprima 
un saludo. Luego, el programa debe pedir el nombre del usuario y llamar a la función. 
"""
def saludar(nombre:str):
    print(f"Saludos {nombre}")
    
    
nombre = input("Ingrese su nombre de usuario")
saludar(nombre)
"""
2. Escribir una función operaciones(num1, num2) que reciba dos números y muestre su suma, 
resta y multiplicación. Luego, el programa debe pedir dos números al usuario y llamar a la 
función. 
3. Definir una función area_triangulo que reciba la base y la altura de un triángulo y 
devuelva su área. Luego, el programa debe pedir los valores y mostrar el resultado.  
Fórmula: area = (b * h) / 2. 
4. Crear una función buscar_mayor que reciba tres números y devuelva los tres números 
ordenados de mayor a menor. Luego, el programa debe pedir los números y mostrar los números 
ordenados. 
5. Definir una función es_par(numero) que reciba un número y devuelva True si es par y False si 
es impar. Luego, el programa debe pedir un número y mostrar si es par o impar usando la función. 
6. Crear una función convertir_minutos(minutos) que reciba una cantidad de minutos y devuelva 
cuántas horas y minutos sobran. 
7. Escribir una función verificar_acceso(edad) que reciba la edad de una persona y determine si 
es mayor de edad (18 años o más) devolviendo un booleano. Luego, el programa debe pedir la 
edad al usuario y mostrar un mensaje apropiado. 
8. Crear una función llamada calcular_edad(anio_nacimiento) que reciba el año de nacimiento y 
devuelva la edad actual (sin considerar el mes de nacimiento). Luego, el programa debe pedir el 
año de nacimiento del usuario y mostrar la edad calculada. 
"""