'''Nombre de la materia 
Martín Alejandro García 
Práctica Listas y Funciones 
Sistema de Catálogo de Biblioteca 
Listas estáticas y funciones 
Una biblioteca escolar necesita un pequeño sistema de gestión para su catálogo de libros. 
Se deben usar listas estáticas con un máximo de 20 títulos y sus respectivos ejemplares. 

Requerimientos: 
1. 
Usar dos listas paralelas: 
1. 
titulos[] → nombres de los libros. 
2. ejemplares[] → cantidad de copias disponibles. 
Cada índice representa el mismo libro en ambas listas. 
2. Implementar un menú de opciones utilizando un bucle while que se repita hasta que el usuario elija 
Salir. 
3. Opciones del menú: 
1. 
Cargar títulos y ejemplares 
Permitir al usuario ingresar hasta 20 títulos y la cantidad de ejemplares para cada uno. 
2. Mostrar catálogo completo 
Listar cada título con su número de ejemplares. 
Ejemplo: El Señor de los Anillos → 5 copias 
3. Consultar disponibilidad 
Pedir al usuario un título y mostrar cuántas copias tiene. 
4. Listar títulos agotados 
Mostrar solo aquellos títulos que tengan 0 copias. 
5. Agregar un nuevo título 
Permitir al usuario agregar un nuevo libro y su cantidad de ejemplares si no se superó el máximo 
de 20. 
6. Actualizar ejemplares (préstamo / devolución) 
Permitir al usuario modificar el número de ejemplares de un libro existente. 
7. 
Salir 
Ejemplo de listas paralelas: 
titulos = ["El Señor de los Anillos", "Orgullo y Prejuicio", "Matar un Ruiseñor"] 
ejemplares = [5, 3, 7] 
Puntos clave: 
● Usar listas estáticas de tamaño fijo ([""] * 20 y [0] * 20). 
● Manejar correctamente los índices para mantener sincronizados títulos y ejemplares. 
● Evitar sobrepasar el límite de 20 elementos. 
● Modularizar usando funciones para cada opción del menú. 
1 '''

import funciones as f


titulos_vacios = True
condicion = "s"
MAXIMO_LIBROS = 20
titulos = [""] * MAXIMO_LIBROS
ejemplares = [0] * MAXIMO_LIBROS
salir = True

while salir:
    print("1. Cargar títulos y ejemplares ")
    print("2. Mostrar catálogo completo ")
    print("3. Consultar disponibilidad ")
    print("4. Listar títulos agotados ")
    print("5. Agregar un nuevo título ")
    print("6. Actualizar ejemplares (préstamo / devolución) ")
    print("7. Salir")

    opcion = input("Ingrese una opcion: ")
    if opcion == "1":
        if titulos_vacios == True:
            print("Para terminar de cargar datos presione ñ")
            f.cargar_titulos(titulos, ejemplares)
            titulos_vacios = False
        else:
            condicion = input("Ya ingreso los datos, desea volver a ingresarlos otra vez?: (s/n)")
            while condicion != "s":
                print("Error. Ingrese 's' o 'n'")
                condicion = input("Ya ingreso los datos, desea volver a ingresarlos otra vez?: (s/n)")

            if condicion == "s":
                f.cargar_titulos(titulos, ejemplares)

    elif opcion == "2":
        f.mostrar_catalogo(titulos, ejemplares)
    elif opcion == "3":
        f.consultar_disponibilidad(titulos, ejemplares)
    elif opcion == "4":
        f.listar_titulos_agotados(titulos, ejemplares)
    elif opcion == "5":
        f.agregar_titulo(titulos, ejemplares)
    elif opcion == "6":
        f.actualizar_ejemplares(titulos, ejemplares)
    elif opcion == "7":
        salir = False