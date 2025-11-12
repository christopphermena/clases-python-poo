#Encapsulamiento
#Atributos y métodos, públicos, privados y protegidos

#Encapsulamiento es el principio de ocultar o mostrar lo que yo quiera

#Para trabajar con atributos privados debemos usar 2 métodos: getter() y setter()
#Getter me permite acceder al atributo privado
#Setter me permite modificar el atributo privado
#Lo hacen de forma controlada, respetando el encapsulamiento
#El atributo no se accede directamente, sino que a través de estos métodos

#Cuando decidimos si un atributo es privado:
#-Cuando son datos sensibles
#-Para validar datos antes de guardarlos
#-Para evitar cambios no deseados
#-Para mantener el control dentro de la clase

#En Python, como declaramos atributos:
#-privados __nombreatributoprivado
#-protegidos _nombreatributoproyegido
#-publicos nombreatributopublico

#Para acceder a los atributos privados usamos getter()

class Persona():
    #Constructor
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.__edad=edad

    #Para acceder al atributo privado __edad
    def get_edad(self):
        return self.__edad
    
    #Para modificar el atributo privado __edad
    def set_edad(self,nueva_edad):
        if nueva_edad > 0:
            self.__edad=nueva_edad
        else:
            print("La edad tiene que ser mayor a 0")

    def MostrarInformacion(self):
        print(f"La edad de la persona es {self.__edad}")
    

objetoPersona = Persona("Macarena",40)

#Quiero imprimir la edad
print("\n")
objetoPersona.MostrarInformacion()
print(objetoPersona.get_edad())
#Quiero modificar la edad
print("\n")
print(objetoPersona.set_edad(30))
