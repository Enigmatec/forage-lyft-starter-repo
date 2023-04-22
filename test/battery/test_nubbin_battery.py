import unittest
from datetime import datetime
from battery.nubbin import NubbinBattery


class TestNubbinBattery(unittest.TestCase):

    def test_splinder_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)

        nubbin_battery = NubbinBattery(last_service_date, today)
        self.assertTrue(nubbin_battery.needs_service())

    def test_nubbine_battery_should_be_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)

        nubbin_battery = NubbinBattery(last_service_date, today)
        self.assertFalse(nubbin_battery.needs_service())

if __name__ == '__main__':
    unittest.main()