class Account:
    id       = int
    nombre   = str
    edad     = int
    mail     = str
    telefono = int 
    
    def __init__(self, id, nombre, edad, email, telefono):
        self.id      = id
        self.nombre  = nombre
        self.edad    = edad
        self.mail    = email
        self.telefono= telefono
        