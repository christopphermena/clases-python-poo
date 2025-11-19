from abc import ABC, abstractmethod

class Vehiculo(ABC):
    @abstractmethod
    def tocar_bocina(self):
        pass #Implemento clases hijas.
    
class Auto(Vehiculo):
    def tocar_bocina(self):
        print(f"El auto hace: Pii piii")
    
class Tren(Vehiculo):
    def tocar_bocina(self):
        print(f"El tren hace: tuuu tuuu")
    
    
objeto_auto = Auto()
objeto_tren = Tren()

objeto_auto.tocar_bocina()
objeto_tren.tocar_bocina()