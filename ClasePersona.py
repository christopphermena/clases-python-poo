#Construir la clase persona
class Persona():
    #Constructor, 2 atributos: nombre y edad
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad

    #Métodos
    def SaludarPersona(self):
        print(f"Hola {self.nombre}, bienvenido(a) a este curso.")

    def MostrarEdad(self):
        print(f"{self.nombre} tiene {self.edad} años.")

#Crear objetos
objetoPersona1=Persona("Macarena",45)
objetoPersona2=Persona("Alejandra",54)

#Usar los métodos
objetoPersona1.SaludarPersona()
objetoPersona2.MostrarEdad()

#Construir subclase Estudiante (herencia)
class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera, semestre):
        super().__init__(nombre, edad)
        self.carrera = carrera
        self.semestre = semestre
 

    #Crear los metodos para estudiante combinados con la clase padre
    def MostrarInformacion(self):
        print(f"Nombre: {self.nombre},\nEdad: {self.edad},\nCarrera: {self.carrera},\nSemestre: {self.semestre}")
    
    def MostrarCumplirAnios(self):
        self.edad += 1
        print(f"{self.nombre} ahora tiene {self.edad} años.")
    
    
#Crear objetos de la clase Estudiante
PersonaEstudiante1 = Estudiante("Juan", 30, "Analista Programador", 1) 
PersonaEstudiante2 = Estudiante("Felipe", 20, "Analista Programador", 2) 
    
#Usar los metodos de los estudiantes
#Informacion del estudiante
PersonaEstudiante1.MostrarInformacion()
#Años cumplidos del estudiante
PersonaEstudiante2.MostrarCumplirAnios()

#Saludo del estudiante (método heredado de la clase Persona)
PersonaEstudiante1.SaludarPersona()
    
#Tarea para la casa ...la traen el miércoles
#Implementar herencia con la clase Persona
#Superclase va a ser Persona()
#Subclase va a ser Estudiante()
#Los atributos de Estudiante son: carrera, semestre
#Los métodos de Estudiante 1) MostrarInformacion() --> mostrar toda la información del estudiante: nombre, edad, carrera y semestre 
#2) CumplirAnios() --> a la edad ingresada le van a sumar 1