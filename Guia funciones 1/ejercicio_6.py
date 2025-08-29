"""6. Crear una función convertir_minutos(minutos) que reciba una cantidad de minutos y devuelva 
cuántas horas y minutos sobran. 
"""
def convertir_minutos(minutos:int) -> bool:
    horas = minutos // 60
    minutos_sobrantes = minutos % 60
    return horas, minutos_sobrantes

minutos = int(input("Ingrese una cantidad de minutos: "))
horas, minutos_sobrantes = convertir_minutos(minutos)
print(f"{horas}:{minutos_sobrantes}")