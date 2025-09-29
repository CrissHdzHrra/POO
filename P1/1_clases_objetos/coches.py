"""
-marca, color, velocidad, modelo, caballaje y plazas en privado
acelerar y frenar en publico (Sin modificar)
"""
import os
os.system("cls")
class Coches:
    __color=""
    __modelo=""
    __velocidad=0
    __caballaje=0
    __plazas=0

    def Acelerar(self,incremento):
        self.__velocidad=incremento+self.__velocidad
        print(self.__modelo)
        return self.__velocidad
    
    def Frenar(self,decremento):
        self.__velocidad=self.__velocidad-decremento
        return self.__velocidad
    
    def get_info(self):
        return f"Marca: {self.marca}, Color: {self.color}, Modelo: {self.__modelo}, Velocidad: {self.__velocidad}, Caballaje: {self.__caballaje}, Plazas: {self.__plazas}"
    
#Crear objetos
coche1=Coches()
coche1.marca="VM"
coche1.color="Blanco"
coche1.modelo="2022"
coche1.velocidad=220
coche1.caballaje=150
coche1.plazas=5

coche2=Coches()
coche2.marca="Nissasn"
coche2.color="Azul"
coche2.modelo="2020"
coche2.velocidad=180
coche2.caballaje=150

print(coche1.get_info())
print(coche2.get_info())
