"""
Ejercicio practico #2 - Modelar y diagramar en POO

"""
import os
os.system('cls')

#Clase de coches
class Coches:
    def __init__(self,color,marca,velocidad): #metodo constructor que inicializa los valores cuando se instancia un objeto de la clase :V
        self.__color=color #Atributos
        self.__marca=marca #Agrega dos giones bajos para convertir un atributo a privado __
        self.__velocidad=velocidad
        self.__modelo=2020

    #Metodos del objeto
    def getColor(self): #privado
        return self.__color

    def getmarca(self): #privado
        return self.__marca

    def Velocidad(self): #privado
        return self.__velocidad

    def Acelerar(self,incremento): #Metodos
            self.__velocidad=incremento+self.__velocidad
            print(self.__modelo)
            return self.__velocidad

    def Frenar(self,decremento): #Metodos
            self.__velocidad=self.__velocidad-decremento
            return self.__velocidad

    def tocarclaxon(self): 
            print ("pipipipipipipippiip")
    #Otro metodo para mostrar la informacion del coche sin necesidad de imprimir una clase hija por otra sucesivamente
    def get_info(self): 
        return f"los valores del coche son: Color: {self.getColor()}, Marca: {self.getmarca()}, Velocidad: {self.Velocidad()}"
    #De esta manera ahorraas mas codigo
    def infovelocidad(self):
        return f"El coche acelero de {self.Velocidad()} a {self.Acelerar(60)}"
    #instanciar o crear objetos de la clase COCHES

coche1=Coches("Blanco","Toyota",160)
coche2=Coches("Amarillo","Nissan",120)

print(coche1.get_info())
print(coche1.infovelocidad())

print(coche2.get_info())
print(f"el coche 2 freno de {coche2.Velocidad()} a {coche2.Frenar(100)}")

"""
print(f"Los valores del objeto 1 son: {coche1.getmarca()}, el color es: {coche1.getColor()} y la velocidad es de: {coche1.Velocidad()} kilometros por hora")

print(f"El coche 1 acelero de {coche1.Velocidad()} a {coche1.Acelerar(60)} ")

print(f"Los valores del objeto 2 son: {coche2.getmarca()}, el color es: {coche2.getColor()} y la velocidad es de: {coche2.Velocidad()} kilometros por hora")
coche2.Frenar(100)
print(f"El coche2  freno de {coche2.Velocidad()} a {coche2.Frenar(50)} ")


Otra alternativa -No recomendable-

Coche():
    color=Blanco
    marca=Toyota
    velocidad=160
    
coche1=Coche()
print(coche1.marca)

"""