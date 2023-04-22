import unittest
from datetime import datetime
from car import CarFactory
from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin import NubbinBattery
from battery.splindler import SplindlerBattery


class TestCarFactory(unittest.TestCase):
    def test_calliope_car_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        calliope_car = CarFactory.create_calliope(today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(calliope_car.needs_service())

    def test_calliope_car_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        calliope_car = CarFactory.create_calliope(today, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(calliope_car.needs_service())

    def test_calliope_car_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0

        calliope_car = CarFactory.create_calliope(today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(calliope_car.needs_service())

    def test_calliope_car_engine_should_be_not_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0

        calliope_car = CarFactory.create_calliope(today, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(calliope_car.needs_service())

    def test_glisade_car_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        glisade_car = CarFactory.create_glissade(today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(glisade_car.needs_service())
    
    def test_glisade_car_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        glisade_car = CarFactory.create_glissade(today, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(glisade_car.needs_service())

    def test_glisade_car_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0

        glisade_car = CarFactory.create_glissade(today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(glisade_car.needs_service())

    def test_glisade_car_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0

        glisade_car = CarFactory.create_glissade(today, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(glisade_car.needs_service())

    def test_palindrome_car_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        warning_light_is_on = False

        palindrome_car = CarFactory.create_palindrome(today, last_service_date, warning_light_is_on)
        self.assertTrue(palindrome_car.needs_service())

    def test_palindrome_car_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        warning_light_is_on = False

        palindrome_car = CarFactory.create_palindrome(today, last_service_date, warning_light_is_on)
        self.assertFalse(palindrome_car.needs_service())

    def test_palindrome_car_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        warning_light_is_on = True

        palindrome_car = CarFactory.create_palindrome(today, last_service_date, warning_light_is_on)
        self.assertTrue(palindrome_car.needs_service())

    def test_palindrome_car_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        warning_light_is_on = False

        palindrome_car = CarFactory.create_palindrome(today, last_service_date, warning_light_is_on)
        self.assertFalse(palindrome_car.needs_service())

    def test_rorschach_car_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        rorschach_car = CarFactory.create_rorschach(today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(rorschach_car.needs_service())

    def test_rorschach_car_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        rorschach_car = CarFactory.create_rorschach(today, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(rorschach_car.needs_service())

    def test_rorschach_car_engine_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0

        rorschach_car = CarFactory.create_rorschach(today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(rorschach_car.needs_service())

    def test_rorschach_car_engine_be_not_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0

        rorschach_car = CarFactory.create_rorschach(today, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(rorschach_car.needs_service())

    def test_thovex_car_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        thovex_car = CarFactory.create_thovex(today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(thovex_car.needs_service())

    def test_thovex_car_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        thovex_car = CarFactory.create_thovex(today, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(thovex_car.needs_service())

    def test_thovex_car_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0

        thovex_car = CarFactory.create_thovex(today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(thovex_car.needs_service())

    def test_thovex_car_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0

        thovex_car = CarFactory.create_thovex(today, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(thovex_car.needs_service())


if __name__ == '__main__':
    unittest.main()
