import os
os.system("cls")

class Coches:
    def __init__(self,marca,color,modelo,velocidad,potencia,plazas):
        self._marca=marca
        self._color=color
        self._modelo=modelo
        self._velocidad=velocidad
        self._potencia=potencia
        self._plazas=plazas
    @property
    def marca(self):
        return self._marca
    @marca.setter
    def marca(self,marca):
        self._marca=marca
    @property
    def color(self):
        return self._color
    @color.setter
    def color(self, color):
        self._color = color
    @property
    def modelo(self):
        return self._modelo
    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo
    @property
    def velocidad(self):
        return self._velocidad
    @velocidad.setter
    def velocidad(self, velocidad):
        self._velocidad = velocidad
    @property
    def potencia(self):
        return self._potencia
    @potencia.setter
    def potencia(self, potencia):
        self._potencia = potencia
    @property
    def plazas(self):
        return self._plazas
    @plazas.setter
    def plazas(self, plazas):
        self._plazas = plazas
    def acelerar(self):
        return "Estoy acelerando el coche"
    def frenar(self):
        return "Estoy frenando el coche"

class Camiones(Coches):
    def __init__(self, marca, color, modelo, velocidad, caballaje, plazas,eje,capacidadCarga):
        super().__init__(marca, color, modelo, velocidad, caballaje, plazas)
        self.__eje=eje
        self.__capacidadCarga=capacidadCarga

    @property
    def eje(self):
        return self.__eje
    @eje.setter
    def eje(self, eje):
        self.__eje = eje
    @property
    def capacidadCarga(self):
        return self.__capacidadCarga
    @capacidadCarga.setter
    def capacidadCarga(self, capacidadCarga):
        self.__capacidadCarga = capacidadCarga

    def acelerar(self):
        return "Estoy acelerando el camion"
    def frenar(self):
        return "Estoy frenando el camion"
    def cargar(self,tipo_carga):
        self.__tipo_carga=tipo_carga
        return f"Estoy cargando el camion con {self.__tipo_carga}"
    
class Camionetas(Coches):
    def __init__(self, marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada):
        super().__init__(marca, color, modelo, velocidad, caballaje, plazas)
        self.__traccion=traccion
        self.__cerrada=cerrada
    @property
    def traccion(self):
        return self.__traccion
    @traccion.setter
    def traccion(self, traccion):
        self.__traccion = traccion
    @property
    def cerrada(self):
        return self.__cerrada
    @cerrada.setter
    def tipo(self, cerrada):
        self.__cerrada = cerrada
    def acelerar(self):
        return "Estoy acelerando la camioneta"
    def frenar(self):
        return "Estoy frenando la camioneta"
    def trasportar(self,num_pasajeros):
        return f"Estoy transportando {num_pasajeros} pasajeros en la camioneta"