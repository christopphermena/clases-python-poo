#Polimorfismo
#Clase SuperClase o clase padre
class Animal():
    def HacerSonido(self):
        pass

        
#SubClases o Clases Hijas
class Perro(Animal):
    def HacerSonido(self):
        print(f"El perro dice: Guau Guau")
        
class Gato(Animal):
    def HacerSonido(self):
        print("El gato dice: Miauuuuuuu")
        
class Pollo(Animal):
    def HacerSonido(self):
        print("El pollo dice: pio pio")
        
#Crear objetos

ObjetoPerro = Perro()
ObjetoPerro.HacerSonido()

ObjetoGato = Gato()
ObjetoGato.HacerSonido()

ObjetoPollo = Pollo()
ObjetoPollo.HacerSonido()

#Crear Lista de los objetos de las clases hijas
ObjetosAnimales = [Perro(), Gato(), Pollo()]

for i in ObjetosAnimales:
    i.HacerSonido()
    






