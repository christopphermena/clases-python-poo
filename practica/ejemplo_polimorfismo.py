class Vehiculo():
    def tocar_bocina(self):
        pass
    
class Tren(Vehiculo):
    def tocar_bocina(self):
        print(f"El tren hace: Tuuu tuuuuuu...")
        
class Auto(Vehiculo):
    def tocar_bocina(self):
        print(f"El auto hace: Piii piiiiii...")
        
objeto_tren = Tren()
objeto_auto = Auto()

objeto_tren.tocar_bocina()
objeto_auto.tocar_bocina()