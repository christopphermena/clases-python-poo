#Abstraccion
from abc import ABC, abstractmethod

#SuperClase abstracta
class Forma(ABC):
    @abstractmethod
    def CalcularArea(self):
        pass #Lo voy a implementar en las clases hijas o subclases
    
    def CalcularPerimetro(self):
        pass #Lo voy a implementar en las clases hijas o subclases
    
#Clase hija o subclase
class Cuadrado(Forma):
    #Inicializar atributos
    def __init__(self, lado):
        self.lado = lado
        
    def CalcularArea(self):
        area = self.lado**2
        return print(f"El area del cuadraddo es: {area}")
    
    def CalcularPerimetro(self):
        perimetro = self.lado * 4
        return print(f"El perimetro del cuadrado es: {perimetro}")

class Circulo(Forma):
    #Inicializar atributos
    def __init__(self, radio):
        self.radio = radio
        
    def CalcularArea(self):
        area = 3.14 * (self.radio**2)
        return print(f"El area del circulo es: {area}")
    
    def CalcularPerimetro(self):
        perimetro = 2 * 3.14 * self.radio
        return print(f"El perimetro del circulo es: {perimetro}")
    
#Crear objetos de las clases hijas
ObjetoCuadrado = Cuadrado(3)
ObjetoCirculo = Circulo(3)

#Uso de los metodos en los objetos
ObjetoCuadrado.CalcularArea()
ObjetoCuadrado.CalcularPerimetro()

print("\n--------\n")

ObjetoCirculo.CalcularArea()
ObjetoCirculo.CalcularPerimetro()