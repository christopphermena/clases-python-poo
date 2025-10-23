#Superclase o Clase Padre
class Animal():
    #Inicializar
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def HacerSonido(self):
        print("El animal hace un sonido")
    
    def MostrarInformacion(self):
        print(f"Nombre: {self.nombre} - edad: {self.edad}")

#Crear Metodos de las subclases o Clases Hijas        
class Perro(Animal):
    def HacerSonido(self):
        print(f"{self.nombre} dice: Guau Guau")
        
class Gato(Animal):
    def HacerSonido(self):
        print(f"{self.nombre} dice: Miauuuuuuu")

#Crear objetos        
ObjetoPerro = Perro("Darwin", 9)
ObjetoGato = Gato("Mango", 1)

#Usar los metodos de las clases hijas
ObjetoPerro.MostrarInformacion() #Metodo heredado del padre
ObjetoGato.HacerSonido() #Metodo a traves del polimorfismo


        