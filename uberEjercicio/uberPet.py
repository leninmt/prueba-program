from car import Car

class UberXL(Car):
    TrasportePet  = bool
    
    def __init__(self, placa, modelo , color, año, matricula, driver,transportePet):
        super().__init__(placa, modelo , color, año, matricula, driver)
        self.TrasportePet = transportePet