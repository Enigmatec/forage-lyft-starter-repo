import unittest
from datetime import datetime
from engine.sternman_engine import SternmanEngine


class TestSternmanEngine(unittest.TestCase):

    def test_capulet_engine_should_be_serviced(self):
        warning_light_is_on = True
        sternman_engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(sternman_engine.needs_service)

    def test_sternman_engine_should_not_be_serviced(self):
        warning_light_is_on = False
        sternman_engine = SternmanEngine(warning_light_is_on)
        self.assertFalse(sternman_engine.needs_service)