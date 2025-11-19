#Creacion de clase
class Persona():
    #Constructor
    def __init__(self, nombre, rut):
        self.nombre = nombre
        self.rut = rut
        
    #Metodos    
    def info_persona(self):
        print(f"Nombre de cliente: {self.nombre} \nRut del cliente: {self.rut}")

#Subclase
class Estudiante(Persona):
    def __init__(self, nombre, rut, asignatura, curso):
        super().__init__(nombre, rut)
        self.asignatura = asignatura
        self.curso = curso
    
    #Metodo subclase
    def info_estudiante(self):
        print(f"El estudiante: {self.nombre}, tiene asignado el curso: {self.curso}.");
        print(f"Asignatura: {self.asignatura}")    
        
#Objetos    
objeto_cliente = Persona("Juan", "20.113.744-6")
objeto_estudiante = Estudiante("Felipe", "20.113.732-2", "Analista", "C3")

#Llamada
objeto_cliente.info_persona()
objeto_estudiante.info_estudiante()

