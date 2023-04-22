from tyre.tyre import Tyre
import constant

class CarriganTyre(Tyre):
    def __init__(self, tire_wear_array:list):
        self.tire_wear_array = tire_wear_array

    def needs_service(self):
        for tire_array in self.tire_wear_array:
            if tire_array >= 0.9:
                return True
        return False