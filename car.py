from abc import ABC, abstractmethod
from datetime import date

from engine.engine import Engine
from battery.battery import Battery
from tyre.tyre import Tyre

from battery.nubbin import NubbinBattery
from battery.splindler import SplindlerBattery

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

from tyre.carrigan_tyre import CarriganTyre
from tyre.octoprime_tyre import OctoprimeTyre


class Serviceable(ABC):
    @abstractmethod
    def needs_service(self):
        pass

class Car(Serviceable):
    def __init__(self, battery:Battery, engine:Engine, tyre: Tyre):
        self.battery = battery
        self.engine = engine
        self.tyre = tyre

    def needs_service(self):
        return self.battery.needs_service() or self.engine.needs_service() or self.tyre.needs_service()


class CarFactory:
    @staticmethod
    def create_calliope(current_date:date, last_service_date:date, current_mileage:int, last_service_mileage:int, tire_wear_array:list):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SplindlerBattery(last_service_date, current_date)
        tyre = OctoprimeTyre(tire_wear_array)
        car = Car(battery=battery, engine=engine, tyre=tyre)
        return car
    
    @staticmethod
    def create_glissade(current_date:date, last_service_date:date, current_mileage:int, last_service_mileage:int, tire_wear_array:list):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SplindlerBattery(last_service_date, current_date)
        tyre = OctoprimeTyre(tire_wear_array)
        car = Car(battery=battery, engine=engine, tyre=tyre)
        return car
    
    @staticmethod
    def create_palindrome(current_date:date, last_service_date:date, warning_light_is_on:bool, tire_wear_array:list):
        engine = SternmanEngine(warning_light_is_on=warning_light_is_on)
        battery = SplindlerBattery(last_service_date, current_date)
        tyre = CarriganTyre(tire_wear_array)
        car = Car(battery=battery, engine=engine, tyre=tyre)
        return car
    
    @staticmethod
    def create_rorschach(current_date:date, last_service_date:date, current_mileage:int, last_service_mileage:int, tire_wear_array:list)->Car:
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tyre = CarriganTyre(tire_wear_array)
        car = Car(battery=battery, engine=engine, tyre=tyre)
        return car
    
    @staticmethod
    def create_thovex(current_date:date, last_service_date:date, current_mileage:int, last_service_mileage:int, tire_wear_array:list)->Car:
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tyre = CarriganTyre(tire_wear_array)
        car = Car(battery=battery, engine=engine, tyre=tyre)
        return car
    