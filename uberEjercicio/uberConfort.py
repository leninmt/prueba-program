from car import Car

class UberXL(Car):
    asientos   = int
    tapizado   = str
    aceptado   = bool
    
    def __init__(self, placa, modelo , color, año, matricula, driver,asientos, tapizado, aceptado):
        super().__init__(placa, modelo , color, año, matricula, driver)
        self.asientos = asientos
        self.tapizado  = tapizado
        self.aceptado  = aceptado