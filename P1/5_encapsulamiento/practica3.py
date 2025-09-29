
"""
Crea un sistema escolar con alumnos, cursos y profesores

"""

class Alumnos:
    def __init__(self, nombre, edad, matricula):
        self.__nombre=nombre
        self.__edad=edad
        self.__matricula=matricula
        

    def getNombre(self): #privado
        return self.__nombre
    def setNombre(self,nombre):
        self.__nombre=nombre

    def getEdad(self): #privado
        return self.__edad
    def setNombre(self,edad):
        self.__edad=edad

    def getMatricula(self): #privado
        return self.__matricula
    def setMatricula(self,matricula):
        self.__matricula=matricula

    def Estudiar(self):
        pass
    def Inscribirse(self):
        pass    

class Profesores:
    def __init__(self, nombre, experiencia, num_profesor):
        self.__nombre=nombre
        self.__experiencia=experiencia
        self.__num_profesor=num_profesor

    def getNombre(self):
        return self.__nombre
    def setNombre(self, nombre):
        self.__nombre=nombre

    def getExperiencia(self):
        return self.__experiencia
    def setExperiencia(self, experiencia):
        self.__experiencia=experiencia

    def getNumProfesor(self):
        return self.__num_profesor
    def setNumProfesor(self, num_profesor):
        self.__num_profesor=num_profesor

    # Métodos adicionales
    def impartir(self):
        pass
    def evaluar(self):
        pass

class Cursos:
    def __init__(self, nombre, codigo, creditos):
        self.__nombre=nombre
        self.__codigo=codigo
        self.__creditos=creditos

    def getNombre(self):
        return self.__nombre
    def setNombre(self, nombre):
        self.__nombre=nombre

    def getCodigo(self):
        return self.__codigo
    def setCodigo(self, codigo):
        self.__codigo=codigo

    def getCreditos(self):
        return self.__creditos
    def setCreditos(self, creditos):
        self.__creditos=creditos

    def Asignar(self):
        pass
        

alumno1=Alumnos("Juan Contreras simental",22,100123)
alumno2=Alumnos("Maria Serrano Mata",22,100124)

profesor1=Profesores("Ana torres Guzman",40,123)
profesor2=Profesores("Daniel Contreras",35,124)

curso1=Cursos("POO",100,6)
curso2=Cursos("FOSO",101,4)



