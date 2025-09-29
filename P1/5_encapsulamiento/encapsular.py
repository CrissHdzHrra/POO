"""

# El encapsulamiento es un pilar de la poo que permite indicar cual es la manera de como poder utilizar
los atributos de una clase a la hora de usar en objetos o en herencia que es otro pilar

"""
import os
os.system("cls")

class Clase:
    atributo_publico="Soy un atributo publico"
    _atributo_protegido="Soy un atributo protegido"
    __atributo_privado="Soy un atributo privado"
    def __init__(self,color,tamanio):
        self.color=color #publico
        self.__tamanio=tamanio #privado
#despues de crear un constructor ocupas especificar que necesitas al momento de usar una clase

    #color
    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self,color):
        self.__color=color
    #Tamaño
    @property
    def tamanio(self):
        return self.__tamanio
    @tamanio.setter
    def tamanio(self,tamanio):
        self.__tamanio=tamanio

    #PUBLICO
    @property
    def atributopublico(self):
        return self.atributo_publico
    @atributopublico.setter
    def atributopublico(self,atributo_publico):
        self.atributo_publico=atributo_publico
    #PROTEGIOD
    @property
    def atributo_protegido(self):
        return self.atributo_protegido
    @atributo_protegido.setter
    def atributo_protegido(self,atributo_protegido):
        self.atributo_protegido=atributo_protegido
    #PRIVADO
    @property
    def atributo_privado(self):
        return self.__atributo_privado
    
    @atributo_privado.setter
    def atributo_privado(self,atributo_privado):
        self.__atributo_privado=atributo_privado

#utilizar clase

obj=Clase("Rojo","Grande")
print(obj.color,obj,tamanio)
"""
print(obj.atributo_p) #si no esta en un metodo constructor no se invocará
print(obj._atributo_prot) #Ademas no es buena practica acceder a los valores directamente
"""
#los atributos publicos y protegidos se pueden acceder, los privados no
# print(obj.__atributo_priv) daria algun error
#una forma seria la siguiente
#Solamente puedes acceder si creas un metodo antes

print(obj.atributo_privado)
print(obj.atributopublico)
print(obj.atributo_protegido)