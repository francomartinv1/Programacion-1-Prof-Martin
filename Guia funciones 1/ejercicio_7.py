"""7. Escribir una función verificar_acceso(edad) que reciba la edad de una persona y determine si 
es mayor de edad (18 años o más) devolviendo un booleano. Luego, el programa debe pedir la 
edad al usuario y mostrar un mensaje apropiado. 
"""
def verificar_acceso(edad:int) -> bool:
    if edad >= 18:
        retorno = True
    else:
        retorno = False

    return retorno
edad = int(input("Ingrese su edad: "))
estado = verificar_acceso(edad)
if estado:
    print(f"Usted es mayor de edad, puede pasar")
else:
    print(f"Acceso denegado, debe ser mayor de edad para pasar")