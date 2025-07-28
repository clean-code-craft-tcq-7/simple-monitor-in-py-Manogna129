import unittest
from monitor import vitals_ok

class MonitorTest(unittest.TestCase):
    def test_high_temperature(self):
        self.assertFalse(vitals_ok(103, 75, 98))

    def test_low_temperature(self):
        self.assertFalse(vitals_ok(94, 75, 98))

    def test_low_pulse_rate(self):
        self.assertFalse(vitals_ok(98.6, 59, 98))

    def test_high_pulse_rate(self):
        self.assertFalse(vitals_ok(98.6, 101, 98))

    def test_low_spo2(self):
        self.assertFalse(vitals_ok(98.6, 75, 89))

    def test_all_vitals_normal(self):
        self.assertTrue(vitals_ok(98.6, 75, 95))

    def test_all_vitals_out_of_range(self):
        # Should still return False on first failing check (temperature)
        self.assertFalse(vitals_ok(103, 101, 89))

if __name__ == '__main__':
    unittest.main()
