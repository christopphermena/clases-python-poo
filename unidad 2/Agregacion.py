#Agregación
#Un objeto agrega a otro, pero no lo crea ni lo destruye.
#Ambos existen de forma independiente.
#Es una relación parte-todo débil, porque no dependencia de vida.

class Asignatura():
    #Constructor
    def __init__(self, nombre_asignatura):
        self.nombre_asignatura=nombre_asignatura

class Profesor():
    #Constructor
    def __init__(self, nombre_profesor):
        self.nombre_profesor=nombre_profesor
        #Se da la agregación
        self.asignaturas=[]

    def AgregarAsignatura(self,asignatura: Asignatura):
        #Implemento la agregación porque recibo el objeto que quiero agregar
        self.asignaturas.append(asignatura)

    def MostrarAsignaturasProfesor(self):
        print(f"El profesor {self.nombre_profesor}")
        print("Dicta:")
        for iasignatura in self.asignaturas:
            print(f"- {iasignatura.nombre_asignatura}")

#Usar la agregación
objetoAsignatura1=Asignatura("Bases de Datos Estructuradas")
objetoAsignatura2=Asignatura("Programación Orientada a Objetos Segura")

objetoProfesor=Profesor("Macarena Angulo")
objetoProfesor.AgregarAsignatura(objetoAsignatura1)
objetoProfesor.AgregarAsignatura(objetoAsignatura2)

objetoProfesor.MostrarAsignaturasProfesor()

