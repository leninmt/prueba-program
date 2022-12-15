from payment import Payment

class PaymentCard(Payment):
    banco = str
    numeroCuenta = int
    
    
    
    def __init__(self, id, amount, user, driver, type, valor, fecha, banco, numeroCuenta):
        super().__init__(id, amount, user, driver, type, valor, fecha)
        self.banco        = banco
        self.numeroCuenta = numeroCuenta