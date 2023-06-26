import os
from pathlib import Path
from shutil import copy2
from os import system

mi_ruta = Path(Path.home(), "recetas")

def contador_recetas(ruta):
    contador = 0
    for txt in Path(ruta).glob("**/*.txt"):
        contador+= 1
    return contador

def inicio():
    system('cls')
    print('*'*50)
    print('*' * 5 + " Bienvenido al administrador de recetas " + '*' * 5 )
    print('*'*50)
    print('\n')
    print(f"Las recetas se encuentran en {mi_ruta}")
    print(f"Total recetas: {contador_recetas(mi_ruta)}")
    
    eleccion_menu = 'x'
    opciones_validas = ['1', '2', '3', '4', '5', '6', '7', '8']
    
    while eleccion_menu not in opciones_validas:
        print("Elige una opción: ")
        print('''
              [1] - Leer documento
              [2] - Crear documento nuevo
              [3] - Crear categoría
              [4] - Eliminar documento
              [5] - Eliminar categoría
              [6] - Cambiar nombre a categoría
              [7] - Copiar documento
              [8] - Salir del programa
              ''')
        eleccion_menu = input()
    
    return int(eleccion_menu)

def elegir_categoria(lista):
    eleccion_correcta = None
    
    while eleccion_correcta is None or eleccion_correcta not in range(1, len(lista) + 1):
        try:
            eleccion_correcta = int(input("\nElige una categoría: "))
        except ValueError:
            print("Por favor, ingresa un número válido.")
    
    return lista[eleccion_correcta - 1]

def elegir_receta(lista):
    eleccion_receta = None
    while eleccion_receta is None or eleccion_receta not in range(1, len(lista) + 1):
        try:
            eleccion_receta = int(input("\nElige un documento: "))
        except ValueError:
            print("Por favor, ingresa un número válido.")

    return lista[eleccion_receta - 1]

def mostrar_categorias(ruta):
    print("Categorías")
    ruta_categorias = Path(ruta)
    lista_categorias = []
    contador = 1
    
    for carpeta in ruta_categorias.iterdir():
        carpeta_str = str(carpeta.name)
        print(f"[{contador}] - {carpeta_str}")
        lista_categorias.append(carpeta)
        contador += 1
    
    return lista_categorias

def mostrar_recetas(ruta):
    print("Documentos: ")
    ruta_recetas = Path(ruta)
    lista_recetas = []
    contador = 1
    
    for receta in ruta_recetas.glob('*.txt'):
        receta_str = str(receta.name)
        print(f"[{contador}] - {receta_str}")
        lista_recetas.append(receta)
        contador += 1
    
    return lista_recetas

def leer_receta(receta):
    print(Path.read_text(receta))

def crear_receta(ruta):
    existe = False
    while not existe:
        print("Escribe el nombre de tu documento: ")
        nombre_receta = input() + '.txt'
        print("Escribe tu nuevo documento: ")
        contenido_receta = input()
        ruta_nueva = Path(ruta, nombre_receta)
        
        if not os.path.exists(ruta_nueva):
            with open(ruta_nueva, 'w') as archivo:
                archivo.write(contenido_receta)
            print(f"Tu documento {nombre_receta} ha sido creado")
            existe = True
        else:
            print("Lo siento, ese documento ya existe")

def crear_categoria(ruta):
    existe = False
    while not existe:
        print("Escribe el nombre de la nueva categoría: ")
        nombre_categoria = input()
        ruta_nueva = Path(ruta, nombre_categoria)
        
        if not os.path.exists(ruta_nueva):
            Path.mkdir(ruta_nueva)
            print(f"Tu categoría {nombre_categoria} ha sido creada")
            existe = True
        else:
            print("Lo siento, esa categoría ya existe")

def eliminar_receta(receta):
    Path(receta).unlink()
    print(f"El documento {receta.name} ha sido eliminado")

def eliminar_categoria(categoria):
    Path(categoria).rmdir()
    print(f"La categoría {categoria.name} ha sido eliminada")

def cambiar_nombre_categoria(ruta):
    mis_categorias = mostrar_categorias(ruta)
    mi_categoria = elegir_categoria(mis_categorias)
    nombre_nuevo = input("Ingresa el nuevo nombre para la categoría: ")
    ruta_nueva = Path(mi_categoria.parent, nombre_nuevo)
    mi_categoria.rename(ruta_nueva)
    print(f"El nombre de la categoría se ha cambiado a '{nombre_nuevo}'")

def copiar_documento(ruta):
    mis_categorias = mostrar_categorias(ruta)
    mi_categoria_origen = elegir_categoria(mis_categorias)
    mis_recetas = mostrar_recetas(mi_categoria_origen)

    if len(mis_recetas) < 1:
        print("No hay documentos en esta categoría.")
        return

    mi_receta_origen = elegir_receta(mis_recetas)

    mis_categorias_destino = mostrar_categorias(ruta)
    mi_categoria_destino = elegir_categoria(mis_categorias_destino)

    nombre_nuevo = input("Ingresa el nombre para el documento copiado: ")
    ruta_nueva = Path(mi_categoria_destino, nombre_nuevo + '.txt')

    if os.path.exists(ruta_nueva):
        print("Lo siento, ese documento ya existe")
    else:
        copy2(mi_receta_origen, ruta_nueva)
        print(f"El documento ha sido copiado a {ruta_nueva}")

def volver_inicio():
    eleccion_regresar = 'x'
    while eleccion_regresar.lower() != 'v':
        eleccion_regresar = input("\nPresione V para volver al menú: ")

finalizar_programa = False
while not finalizar_programa:

    menu = inicio()

    if menu == 1:
        mis_categorias = mostrar_categorias(mi_ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        mis_recetas = mostrar_recetas(mi_categoria)
        
        if len(mis_recetas) < 1:
            print("No hay documentos en esta categoría.")
        else:
            mi_receta = elegir_receta(mis_recetas)
            leer_receta(mi_receta)
        
        volver_inicio()

    elif menu == 2:
        mis_categorias = mostrar_categorias(mi_ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        crear_receta(mi_categoria)
        volver_inicio()

    elif menu == 3:
        crear_categoria(mi_ruta)
        volver_inicio()

    elif menu == 4:
        mis_categorias = mostrar_categorias(mi_ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        mis_recetas = mostrar_recetas(mi_categoria)

        if len(mis_recetas) < 1:
            print("No hay documentos en esta categoría.")
        else:
            mi_receta = elegir_receta(mis_recetas)
            eliminar_receta(mi_receta)

        volver_inicio()

    elif menu == 5:
        mis_categorias = mostrar_categorias(mi_ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        eliminar_categoria(mi_categoria)
        volver_inicio()

    elif menu == 6:
        cambiar_nombre_categoria(mi_ruta)
        volver_inicio()

    elif menu == 7:
        mis_categorias = mostrar_categorias(mi_ruta)
        mi_categoria_origen = elegir_categoria(mis_categorias)
        copiar_documento(mi_ruta)

        volver_inicio()

    elif menu == 8:
        finalizar_programa = True
