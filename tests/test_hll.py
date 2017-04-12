import unittest

from hll import HyperLogLog, MartingaleHyperLogLog

class BasicHLLTests(object):
    def test_counts_a_single_element_correctly(self):
        self.hll.add_object(37)
        self.assertAlmostEqual(self.hll.count, 1, delta=0.0001)

    def test_counts_zero_elements_correctly(self):
        self.assertAlmostEqual(self.hll.count, 0, delta=0.0001)


class TestHyperLogLog(unittest.TestCase, BasicHLLTests):
    def setUp(self):
        self.hll = HyperLogLog(16, 16)
        self.hll2 = HyperLogLog(16, 16)

    def test_a_repeated_element_is_ignored(self):
        self.hll.add_object(37)
        self.hll2.add_objects([ 37 for x in range(0, 1000) ])
        self.assertEqual(self.hll.logs, self.hll2.logs)

class TestMartingaleHyperLogLog(unittest.TestCase, BasicHLLTests):
    def setUp(self):
        self.hll = MartingaleHyperLogLog(16, 16)
