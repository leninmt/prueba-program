from payment import Payment
 
class PaymentUberCash(Payment):
    
    def __init__(self, id, amount, user, driver, type, valor, fecha):
        super().__init__(id, amount, user, driver, type, valor, fecha)