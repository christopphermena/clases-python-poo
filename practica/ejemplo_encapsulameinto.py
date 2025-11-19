class Persona():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.__edad = edad
        
    def get_edad(self):
        return self.__edad
    
    def set_edad(self, nueva_edad):
        if nueva_edad > 0:
            self.__edad = nueva_edad
        else:
            print("Ingrese una edad mayor a 0.")
            
    def mostrar_info(self):
        print(f"La edad de {self.nombre}, es {self.__edad}")
        
objeto_persona = Persona("Chris", 26)

print(objeto_persona.get_edad())
objeto_persona.set_edad(35)

print(objeto_persona.get_edad())

objeto_persona.mostrar_info()