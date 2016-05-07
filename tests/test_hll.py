import unittest

from hll import HyperLogLog

class TestHyperLogLog(unittest.TestCase):
    def setUp(self):
        self.hll1 = HyperLogLog(16, 16)
        self.hll2 = HyperLogLog(16, 16)

    def test_a_repeated_element_is_ignored(self):
        self.hll1.add_object(37)
        self.hll2.add_objects([ 37 for x in range(0, 1000) ])
        self.assertEqual(self.hll1.logs, self.hll2.logs)
