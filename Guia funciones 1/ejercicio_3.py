"""3. Definir una función area_triangulo que reciba la base y la altura de un triángulo y 
devuelva su área. Luego, el programa debe pedir los valores y mostrar el resultado.  
Fórmula: area = (b * h) / 2. 
"""
def area_triangulo(base:float, altura:float) -> float:
    area = (base * altura) / 2
    return area

base = int(input("Ingrese la base de un triangulo: "))
altura = int(input("Ingrese la altura de un triangulo: "))
area = area_triangulo(base, altura)
print(f"El area del triangulo es: {area}")