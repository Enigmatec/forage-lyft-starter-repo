import unittest
from datetime import datetime
from battery.splindler import SplindlerBattery


class TestSplidnerBattery(unittest.TestCase):

    def test_splinder_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)

        splinder_battery = SplindlerBattery(last_service_date, today)
        self.assertTrue(splinder_battery.needs_service())

    def test_splinder_battery_should_be_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)

        splinder_battery = SplindlerBattery(last_service_date, today)
        self.assertFalse(splinder_battery.needs_service())