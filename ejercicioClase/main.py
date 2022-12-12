class Persona:
    nombre   = str
    apellido = str
    edad     = str
    
    def __init__(self, nombre, apellido, edad):
        self.nombre   = nombre
        self.apellido = apellido
        self.edad     = edad
        
if __name__== "__main__":
    persona1 = Persona("Alison", "Cumbajin", 21)
    persona2 = Persona("Lenin", "Montalvo",19)
    
    print(persona1.apellido)
    print(persona2.apellido)
    
#La Funciòn _str_ Definir el string que se imprime

class Persona2:
    nombre   = str
    apellido = str
    edad     = str
    carrera  = str
    
    def __init__(self, nombre, apellido, edad, carrera):
        self.nombre   = nombre    
        self.apellido = apellido
        self.edad     = edad
        self.carrera  = carrera
        
    def __str__(self):
        return f'Hola me llamo {self.nombre} {self.apellido}  mi edad es {self.edad} y mi carrera es {self.carrera}'
    
ejemplo1 = Persona2(" Diego"," Yanez", 29, " Desarrollo de Software")
ejemplo2 = Persona2(" Sebastiàn"," Navas", 29," Marketing")
ejemplo3 = Persona2(" Enzo"," Guachilema", 29," Diseño de modas")


print(ejemplo1)
print(ejemplo2)
print(ejemplo3)


#Creación de metodos dentro de objetos


class Persona3: 
    nombre   = str
    apellido = str
    edad     = str
    carrera  = str
    
    def __init__(self, nombre, apellido, edad, carrera, semestre):
        self.nombre   = nombre 
        self.apellido = apellido
        self.edad     = edad
        self.carrera  = carrera
        self.semestre = semestre

    def bu4(self):
        print("Hola " + self.nombre  + self.apellido + " con " + self.edad + " años , " + "Bienvenido a la carrera de " + self.carrera +" ,estás en el  "+ self.semestre )
        
ejemplo4 = Persona3(" Diego"," Yanez", "29", "Desarrollo de Software", "Quinto semestre")
ejemplo5 = Persona3(" Sebastiàn "," Navas", "10","Marketing", "Primer Semestre")
ejemplo6 = Persona3(" Enzo"," Guachilema", "20","Diseño de modas", "Segundo Semestre")

ejemplo4.bu4()
ejemplo5.bu4()
ejemplo6.bu4() 

class Persona:
    nombre   = str
    apellido = str
    edad     = str 
    
    def __init__(self, nombre, apellido, edad):
        self.nombre       = nombre
        self.apellido     = apellido
        self.edad         = edad 
    
        
    def conversar(self, otra_persona):
        return f'Hola {otra_persona}, me llamo {self.nombre}, tengo {self.edad}'

persona1 = Persona("Jordan", " Gonzales",22)
persona2 = Persona("Enzo", " Quishpe",20)        

print(persona1.conversar(persona2))
print(persona1.conversar("Alisson"))