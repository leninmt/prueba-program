from account_user import User
from account_driver import Driver 

class Payment:
    id          = int
    amount      = int
    user        = User("", "", "", "", "")
    driver      = Driver("", "", "", "", "")
    type        = str
    valor       = float
    fecha       = int
    
    def __init__(self, id, amount, user, driver, type, valor, fecha):
        self.id     = id
        self.amount = amount
        self.user   = user
        self.driver = driver
        self.type   = type
        self.valor  = valor
        self.fecha  = fecha
    