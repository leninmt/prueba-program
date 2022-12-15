from car import Car

class UberXL(Car):
    encargo = bool
    pesoMax = int
    def __init__(self, placa, modelo , color, año, matricula, driver, encargo, pesoMax):
        super().__init__(placa, modelo , color, año, matricula, driver)
        self.encargo   = encargo
        self.pesoMax   = pesoMax