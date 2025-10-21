#Construir la clase persona
class Persona():
    #Constructor, 2 atributos: nombre y edad
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad

    #Métodos
    def SaludarPersona(self):
        print(f"Hola {self.nombre}, bienvenido a este curso.")

    def MostrarEdad(self):
        print(f"{self.nombre} tiene {self.edad} años.")

#Crear objetos
objetoPersona1=Persona("Macarena",45)
objetoPersona2=Persona("Alejandra",54)

#Usar los métodos
objetoPersona1.SaludarPersona()
objetoPersona2.MostrarEdad()

#Tarea para la casa ...la traen el miércoles
#Implementar herencia con la clase Persona
#Superclase va a ser Persona()
#Subclase va a ser Estudiante()
#Los atributos de Estudiante son: carrera, semestre
#Los métodos de Estudiante 1) MostrarInformacion() --> mostrar toda la información del estudiante: nombre, edad, carrera y semestre 
#2) CumplirAnios() --> a la edad ingresada le van a sumar 1