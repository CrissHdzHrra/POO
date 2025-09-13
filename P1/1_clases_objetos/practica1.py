"""
Practica 1: Implementar un paradigma estructurado vs OO
...:::Crear un programa que obtenga el area de un rectangulo:::....
"""

#1 Estructurado
def rectangulo():
    print("..:.::..Calculo del area de un rectangulo::::...")
    base = float(input("Introduce la base del rectangulo: "))
    altura = float(input("Introduce altura del rectangulo: "))
    area = base * altura
    print(f"El area del rectangulo es: {area}")
    return area

import os
os.system('cls')
#2 OO
class AreaRectangulo:
    def __init__(self, base, altura):
        print("..:.::..Calculo del area de un rectangulo::::...")
        self.base=base #utiliza self para definir el atributo y que este funcione
        self.altura=altura
        self.area=base*altura

rectangulo1=AreaRectangulo(5,10)
print(f"el area del rectangulo1 es: {rectangulo1.area}")