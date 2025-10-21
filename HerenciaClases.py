#Herencia de clases

#Superclase o clase padre
class Vehiculo():
    #Constructor
    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo

    #Métodos
    def MostrarInformacion(self):
        print(f"Vehículo: {self.marca} - {self.modelo}")
    
    def Encender(self):
        print(f"El {self.marca} - {self.modelo} está encendido...")

#Subclase o clase hija que hereda de Vehiculo
class Automovil(Vehiculo):
    #Constructor
    def __init__(self, marca, modelo,color):
        #Redefinir el constructor para la clase hija
        super().__init__(marca, modelo)
        self.color=color

    def TocarBocina(self):
        print("La bocina suena Piiiiiii piiiiiii")

#Crear objetos
objetoAuto1=Automovil("Mazda","mazda3","blanco")

#Usemos los métodos de la clase padre
objetoAuto1.MostrarInformacion()

#Usemos métodos de la clase hija
objetoAuto1.TocarBocina()