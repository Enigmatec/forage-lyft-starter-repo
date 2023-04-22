from tyre.tyre import Tyre
import constant

class OctoprimeTyre(Tyre):
    def __init__(self, tire_wear_array:list):
        self.tire_wear_array = tire_wear_array

    def needs_service(self):
        return sum(self.tire_wear_array) >= 3