from coches import Coches, Camiones, Camionetas
import os
os.system("cls")

def autos():
    print(f"\n\t...Datos del Vehiculo...")
    marca=input("Ingrese la marca del coche: ").upper()
    color=input("Ingrese el color del coche: ").upper()
    modelo=input("Ingrese el modelo del coche: ").upper()
    velocidad=int(input("Ingrese la velocidad maxima del coche: "))
    potencia=int(input("Ingrese el caballaje del coche: "))
    plazas=int(input("Ingrese el numero de plazas del coche: "))

    coche=Coches(marca,color,modelo,velocidad,potencia,plazas)

    print(f"Datos del Vehiculo \n Marca: {coche.marca()} \n Color: {coche.color()} \n Modelo: {coche.modelo()} \n Velocidad Maxima: {coche.velocidad()} \n Caballaje: {coche.caballaje()} \n Numero de Plazas: {coche.plazas()}")

def camiones():
    print(f"\n\t...Datos del Vehiculo...")
    marca=input("Ingrese la marca del camion: ").upper()
    color=input("Ingrese el color del camion: ").upper()
    modelo=input("Ingrese el modelo del camion: ").upper()
    velocidad=int(input("Ingrese la velocidad maxima del camion: "))
    potencia=int(input("Ingrese el caballaje del camion: "))
    plazas=int(input("Ingrese el numero de plazas del camion: "))
    eje=int(input("Ingrese el numero de ejes del camion: "))
    capacidadCarga=int(input("Ingrese la capacidad de carga del camion (Kg): "))

    camion=Camines(marca,color,modelo,velocidad,potencia,plazas,eje,capacidadCarga)

    print(f"Datos del Vehiculo \n Marca: {camion.marca()} \n Color: {camion.color()} \n Modelo: {camion.modelo()} \n Velocidad Maxima: {camion.velocidad()} \n Caballaje: {camion.caballaje()} \n Numero de Plazas: {camion.plazas()} \n Numero de Ejes: {camion.eje()} \n Capacidad de Carga(Kg): {camion.capacidadCarga()}")

def camionetas():
    print(f"\n\t...Datos del Vehiculo...")
    marca=input("Ingrese la marca de la camioneta: ").upper()
    color=input("Ingrese el color de la camioneta: ").upper()
    modelo=input("Ingrese el modelo de la camioneta: ").upper()
    velocidad=int(input("Ingrese la velocidad maxima de la camioneta: "))
    potencia=int(input("Ingrese el caballaje de la camioneta: "))
    plazas=int(input("Ingrese el numero de plazas de la camioneta: "))
    tracera=input("Ingrese el tipo de eje de la camioneta: ").upper()
    cerrada=bool(input("La camioneta es cerrada (True/False): "))

    camioneta=Camionetas(marca,color,modelo,velocidad,potencia,plazas,tracera,cerrada)

    print(f"Datos del Vehiculo \n Marca: {camioneta.marca()} \n Color: {camioneta.color()} \n Modelo: {camioneta.modelo()} \n Velocidad Maxima: {camioneta.velocidad()} \n Caballaje: {camioneta.caballaje()} \n Numero de Plazas: {camioneta.plazas()} \n Tipo de Eje: {camioneta.tracera()} \n Cerrada: {camioneta.cerrada()}")

opcion=True
while opcion:
    os.system("cls")
    opcion=input("\n\t\t .::Menu Principal::.\n\t 1.-Autos\n\t 2.-Camionetas\n\t 3.-Camiones\n\t 4.-Salir\n\n\t Elige una opcion:")
    match opcion:
        case "1":
            os.system("cls")
            autos()
            input("Oprima una tecla para continuar...")
        case "2":
            os.system("cls")
            print("\n\t...Datos de las Camionetas...")
            input("Oprima una tecla para continuar...")
        case "3":
            os.system("cls")
            print("\n\t...Datos de los Camiones...")
            input("Oprima una tecla para continuar...")
        case "4":
            os.system("cls")
            print("\n\t...Gracias por su visita...")
            input("Oprima una tecla para continuar...")
            opcion=False
        case _:
            os.system("cls")
            print("\n\t...Opcion no valida, vuelva a itentarlo...")
            input("Oprima una tecla para continuar...")
