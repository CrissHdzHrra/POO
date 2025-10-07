"""
-marca, color, velocidad, modelo, caballaje y plazas en privado
acelerar y frenar en publico (Sin modificar)
"""
import os
os.system("cls")
class Coches:
    """
    Metodo cornstructor:
    Con este metodo se inicializa un objeto cuando es creado con valores iniciales
    """
    def __init__(self,marca,color,modelo,velocidad,caballaje,plazas):
        self.__marca=marca
        self.__color=color
        self.__modelo=modelo
        self.__velocidad=velocidad
        self.__caballaje=caballaje
        self.__plazas=plazas 

    """
    #Crear los metodos setters y getters. (Estos metodos son importantes y necesarios en todas las clasess para que el programador interactue con lo valores de los atributos a traves
    de estos metodos). Digamos que ee sla manera mas adecuada y recomendada para solicitar y valor (get) y/o (set) para ingresar o cambiar un valor (set) a un atributo en particular a traves
    de un objeto.

    #En teoria se deberia crear un metodo getters y setters por cada atributo que contenga la clase

    #Los metodos get siempre regresan valor, es decir, el valor de la propiedad a traves del return de otro

    #Por otro lado, el metodo set siempre recibe parametros para cambiar o modificar el valor del atributo o propiedad en cuestion
    """
    
    #-----------------------------PROPIEDADES CON SET Y GET-----------------------------------------------------------------------------
    
    # PRIMERA FORMA ---
    def getMarca(self):
        return self.__marca
    
    def setMarca(self,marca):
        self.__marca=marca

    # SEGUNDA FORMA ---
    @property
    def marca(self):
        return self.__marca
    @marca.setter
    def marca(self,marca):
        self.__marca=marca
    #______________________________-
    def getColor(self):
        return self.__color

    def setColor(self,color):
        self.__color=color

    def getModelo(self):
        return self.__modelo

    def setModelo(self,modelo):
        self.__modelo=modelo

    def getVelocidad(self):
        return self.__velocidad
    
    def setVelocidad(self,velocidad):
        self.__velocidad=velocidad
    
    def getCaballaje(self):
        return self.__caballaje
    
    def setCaballaje(self,caballaje):
        self.__caballaje=caballaje

    def getPlazas(self):
        return self.__plazas
    
    def setPlazas(self,plazas):
        self.__plazas=plazas


    #------------------------------------------------------------------------------------------------------------------------------------

    def Acelerar(self,incremento):
        self.__velocidad=incremento+self.__velocidad
        print(self.__modelo)
        return self.__velocidad
    
    def Frenar(self,decremento):
        self.__velocidad=self.__velocidad-decremento
        return self.__velocidad

#Mulltiples objetos
coche1=Coches()
coche2=Coches()
coche3=Coches()
#Utiliza los metodos set para darle valores a las propiedades o atributos del objeto coche1
coche1.setMarca("VW")
coche1.setColor("Blanco")
coche1.setModelo("2022")
coche1.setVelocidad(220)
coche1.setCaballaje(150)
coche1.setPlazas(5)
coche1.num_serie="123ABC"

coche2.setMarca("Nissan")
coche2.setColor("Azul")
coche2.setModelo("2020")
coche2.setVelocidad(180)
coche2.setCaballaje(150)
coche2.setPlazas(6)

coche3.setMarca("Honda")

#Utiliza los metodos get para obtener los valores de las propiedades o atributos del objeto coche1
print(f'''
Marca: {coche1.getMarca()}
Color: {coche1.getColor()}
Modelo: {coche1.getModelo()}
Velocidad: {coche1.getVelocidad()}
Caballaje: {coche1.getCaballaje()}
Plazas: {coche1.getPlazas()}
''')

print(f'''
Marca: {coche2.getMarca()}  
Color: {coche2.getColor()}
Modelo: {coche2.getModelo()}
Velocidad: {coche2.getVelocidad()}
Caballaje: {coche2.getCaballaje()}
Plazas: {coche2.getPlazas()}
''')


"""
    #Atributos con nombre
coche1.marca=("VM")
coche1=setColor("Blanco")
coche1=setModelo("2022")
coche1=setVelocidad(220)
coche1=setCaballaje(150)
coche1=setPlazas(5)
coche1.num_motor="b345HH7779"

print(f"datos del vehiculo: Marca: {coche1.marca}, Color: {coche1.getColor()}, Modelo: {coche1.getModelo()}, Velocidad: {coche1.getVelocidad()}, Caballaje: {coche1.getCaballaje()}, Plazas: {coche1.getPlazas()}, Numero de Motor: {coche1.num_motor}")


coche2=marca("Nissasn")
coche2=setColor("Azul")
coche2=setModelo("2020")
coche2=setVelocidad(180)
coche2=setCaballaje(150)
coche2.setPlazas(5)

print(f"datos del vehiculo: Marca: {coche2.getMarca()}, Color: {coche2.getColor()}, Modelo: {coche2.getModelo()}, Velocidad: {coche2.getVelocidad()}, Caballaje: {coche2.getCaballaje()}, Plazas: {coche2.getPlazas()}")
"""
    
"""
coche1.marca="VM"
coche1.color="Blanco"
coche1.modelo="2022"
coche1.velocidad=220
coche1.caballaje=150
coche1.plazas=5
coche1.num_motor="b345HH7779"


coche2=Coches()
coche2.marca="Nissasn"
coche2.color="Azul"
coche2.modelo="2020"
coche2.velocidad=180
coche2.caballaje=150

coche3=Coches()
coche3.marca="Honda"


print(coche1.get_info())
print(coche2.get_info())
print(coche3.get_info())

"""


