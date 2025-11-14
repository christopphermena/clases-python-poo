#Abstracción
#Qué es una clase abstracta, es una plantilla general que define como deberían comportarse
#las clases hijas, pero sin implementar completamente este comportamiento.
#No representamos objetos concreto, sino que es una idea o un concepto que la clase abstracta
#puede completar.
#Usamos una librería que ABC utilizamos la clase abc.
#Las clases abstractas no se pueden utilizar directamente, no se pueden instanciar
#se utilizan a través de sus clases hijas.
#Se una un patrón que se llama decorador @abstractmethod

#importación de librerías o módulos
from abc import ABC, abstractmethod

class Transporte(ABC):
    @abstractmethod
    def Mover(self):
        pass

#Implementación
class Tren(Transporte):
    def Mover(self):
        print("El tren sale de la estación.")

class Avion(Transporte):
    def Mover(self):
        print("El avion despega del aeropuerto.")
        
#Uso
objetoTren=Tren()
objetoTren.Mover()

objetoAvion=Avion()
objetoAvion.Mover()