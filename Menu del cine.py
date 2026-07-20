
from os import system
from funciones import*
opc=0
while True:
    print("--------Menu principal-------")
    print("1.- Cupos por genero")
    print("2.- Busqueda de peliculas ")
    print("3.- actualizar precio de pelicula ")
    print("4.- Agregar pelicula ")
    print("5.-eliminar pelicula ")
    print("6.-salir")
    opc=int(input("ingrese una opcion"))

    match(opc):
        case 1:
            cupos_genero()
            input("PRESS ENTER")
            input("cls")
        case 2:
            busqueda_precio()
            input("PRESS ENTER")
            input("cls")
        case 3:
            buscar_codigo()
            input("PRESS ENTER")
            input("cls")
        case 4:
            actualizar_precio()
            input("PRESS ENTER")
            input("cls")
        case 5:
            agregar_pelicula()
            input("PRESS ENTER")
            input("cls")
        case 6:
            cupos_genero()
            input("PRESS ENTER")
            input("cls")
            break