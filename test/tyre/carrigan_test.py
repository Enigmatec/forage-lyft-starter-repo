import unittest
from datetime import datetime
from tyre.carrigan_tyre import CarriganTyre


class TestCarriganTyre(unittest.TestCase):

    def test_carrigan_tyre_should_be_serviced(self):
        carrigan_tyre = CarriganTyre([1, 2, 4, 0.9])
        self.assertTrue(carrigan_tyre.needs_service())

    def test_carrigan_tyre_should_not_be_serviced(self):
        carrigan_tyre = CarriganTyre([0.2, 0.1, 0.8, 0.6])
        self.assertFalse(carrigan_tyre.needs_service())