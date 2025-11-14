#Relaciones entre clases
#Composición
#Es una relación fuerte del todo-parte, donde la parte no existe sin el todo.
#Y los objetos de la parte se componen dentro de la clase todo.
#Clase autor es la parte
class Autor():
    #Constructor
    def __init__(self,nombre_autor):
        self.nombre_autor=nombre_autor

    def MostrarInformacion(self):
        return f"autor: {self.nombre_autor}"

#Clase libro es el todo
class Libro():
    #Constructor
    def __init__(self,titulo, nombre_autor):
        self.titulo=titulo
        #Aquí se da la composición
        self.nombre_autor=Autor(nombre_autor)

    def MostrarInformacionLibro(self):
        print(f"El libro: {self.titulo} del {self.nombre_autor.MostrarInformacion()}")

objetoLibro=Libro("Harry Potter","J.K.Rowling")
objetoLibro.MostrarInformacionLibro()


    