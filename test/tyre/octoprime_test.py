import unittest
from datetime import datetime
from tyre.octoprime_tyre import OctoprimeTyre


class TestOctoprimeTyre(unittest.TestCase):
    
    def test_octoprime_tyre_should_be_serviced(self):
        octoprime_tyre = OctoprimeTyre([1, 2, 3, 4])
        self.assertTrue(octoprime_tyre.needs_service())

    def test_octoprime_tyre_should_not_be_serviced(self):
        octoprime_tyre = OctoprimeTyre([1, 0, 1, 0])
        self.assertFalse(octoprime_tyre.needs_service())