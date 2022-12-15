from car import Car

class UberXL(Car):
    
    def __init__(self, placa, modelo , color, año, matricula, driver):
        super().__init__(placa, modelo , color, año, matricula, driver)
        