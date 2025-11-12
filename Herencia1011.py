#Herencia
#Una super-clase y una subclase
#La subclase hereda los atributos y métodos de su super-clase
#La subclase puede tener su propios atributos y métodos
#El que la subclase pueda heredar atributos y métodos de su super-clase depende de
#la visibilidad de estos.
#Las visibilidades son pública (todos pueden ver), privada (yo y sólo yo) y protegida (yo y mis hijos)

#Cuántos niveles es recomendable agregar en el código - definido por las buenas prácticas de la programación - 
#sea 3 o 4 más de eso se no es una buena práctica

#Todo pública -> atributos y métodos
#La super-clase
class Publicacion():
    #Constructor
    def __init__(self,titulo,autor):
        self.titulo=titulo
        self.autor=autor
    
    def MostrarInformacion(self):
        print(f"Título: {self.titulo} - Autor: {self.autor}")

class Libro(Publicacion):
    #Constructor
    def __init__(self,titulo,autor,editorial,paginas):
        super().__init__(titulo,autor)
        self.editorial=editorial
        self.paginas=paginas

    def Leer(self):
        print(f"Leyendo {self.titulo} de la editorial {self.editorial}")

    #Polimorfismo del enfoque de la POO - polimorfismo por sobreescritura (override)
    def MostrarInformacion(self):
        super().MostrarInformacion()
        print(f"Esta edición tiene {self.paginas} páginas.")

class LibroDigital(Libro):
    #Constructor
    def __init__(self, titulo, autor, editorial, paginas, peso_mb):
        super().__init__(titulo, autor, editorial, paginas)
        self.peso_mb=peso_mb

    def Descargar(self):
        print(f"Descargando {self.titulo} - editorial {self.editorial}, que pesa {self.peso_mb} MB...")

    def MostrarInformacion(self):
        super().MostrarInformacion()
        print(f"Peso del libro digital {self.peso_mb} MB.")


objetoLibro=Libro("Harry Potter - La Piedra Filosofal","J.K.Rowling","Salamandra",200)
objetoLibroDigital=LibroDigital("Los Juegos del Hambre","S.Collins","Salamandra",700,300)

objetoLibro.MostrarInformacion()
print("\n")
objetoLibroDigital.MostrarInformacion()