from account import Account

class User(Account):
    def __init__(self, id, nombre, edad, email, telefono):
        super().__init__(id, nombre, edad, email, telefono)