""" 8. Crear una función llamada calcular_edad(anio_nacimiento) que reciba el año de nacimiento y 
devuelva la edad actual (sin considerar el mes de nacimiento). Luego, el programa debe pedir el 
año de nacimiento del usuario y mostrar la edad calculada. 
"""
def calcular_edad(anio_nacimiento:int) -> int:
    edad = 2025 - anio_nacimiento
    return edad

anio_nacimiento = int(input("Ingrese su año de nacimiento: "))
edad = calcular_edad(anio_nacimiento)
print(f"Usted tiene {edad} años")