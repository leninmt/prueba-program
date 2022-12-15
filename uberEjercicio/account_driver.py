from account import Account

class Driver(Account):
    licencia = str
    def __init__(self, id, nombre, edad, email, telefono, licencia):
        super().__init__(id, nombre, edad, email, telefono)
        self.licencia = licencia