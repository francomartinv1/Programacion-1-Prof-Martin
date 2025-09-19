def cargar_titulos(titulos:list, ejemplares:list):
    contador = 0
    
    while contador < len(titulos):
        titulo = input("Ingrese nombre del titulo: ")
        if titulo == "ñ":
            break
        else:
            titulos[contador] = titulo
        ejemplares[contador] = int(input(f"Ingrese ejemplares de {titulos[contador]}: "))

        contador += 1

def mostrar_catalogo(titulos:list, ejemplares:list):
    if titulos[0] != "":
        print("Catalogo de libros")
        for i in range(len(titulos)):
            if titulos[i] != "":
                print(f"Titulo: {titulos[i]} || Ejemplares: {ejemplares[i]}")
    else:
        print("No hay libros disponibles")
    input("Presiona enter para continuar")

def consultar_disponibilidad(titulos:list, ejemplares:list):
    titulo_elegido = input("Ingrese el titulo a consultar: ")
    bandera = False
    for i in range(len(titulos)):
        
        if titulos[i] == titulo_elegido:
            posicion = i
            bandera = True
            break

    if bandera:
        print(f"El libro {titulos[posicion]} se encuentra disponible")
        print(f"Copias: {ejemplares[posicion]}")
    else:
        print("No encontro el libro con ese nombre")
            
    input("Presiona enter para continuar")

def listar_titulos_agotados(titulos:list, ejemplares:list):
    bandera = False
    contador = 0
    for i in range(len(titulos)):
        if titulos[i] == "":
            break
        if ejemplares[i] == 0:
            contador += 1
            bandera = True
            
    if bandera:
        print("Titulos no dispoibles")
        for i in range(contador):
            if ejemplares[i] == 0:
                print(f"{titulos[i]}")
    else:
        print("No hay titulos no disponibles")
    input("Presiona enter para continuar")

def agregar_titulo(titulos:list, ejemplares:list):
    bandera = False
    for i in range(len(titulos)):
        if titulos[i] == "":
            ultimo_libro = i
            bandera = True
            break
    if bandera:
        titulos[ultimo_libro] = input("Ingrese nombre del titulo: ")
        ejemplares[ultimo_libro] = int(input(f"Ingrese ejemplares de {titulos[ultimo_libro]}: "))
    else:
        print("No se puede agregar mas libros. Maximo alcanzado")

def actualizar_ejemplares(titulos:list, ejemplares:list):
    bandera = False
    titulo = input("Ingrese el titulo que desea actualizar ejemplares: ")
    for i in range(len(titulos)):
        if titulo == titulos[i]:
            print(f"{titulos[i]} tiene {ejemplares[i]} copias")
            cantidad = int(input(f"Ingrese ejemplares del libro {titulo}: "))
            ejemplares[i] += cantidad
            bandera = True

    if not bandera:
        print("No hay titulos con ese nombre")
        input("presiona enter para continuar")