#Creación de la clase Auto()
class Auto():
    #Constructor: inicializan los atributos de la clase Auto 
    #Tiene 3 atributos: marca, modelo y color
    def __init__(self,marca,modelo,color):
        self.marca=marca
        self.modelo=modelo
        self.color=color

    #Métodos de la clase
    def MostrarInformacion(self):
        print(f"Auto: Marca: {self.marca} - modelo: {self.modelo} - color: {self.color}")

    def Arrancar(self):
        print(f"Auto: {self.marca} está arrancando...")

    def Detener(self):
        print(f"Auto: {self.marca} se detuvo...")



###########################################
#Crear (instanciar) objetos de la clase Auto
objetoAuto1=Auto("Toyota","Yaris","gris")   
objetoAuto2=Auto("Nissan","v16","rojo")
objetoAuto3=Auto("Geely","ultimo","magenta")

#Usar los métodos para los objetos
objetoAuto1.MostrarInformacion()

objetoAuto2.Arrancar()

objetoAuto3.Detener()


