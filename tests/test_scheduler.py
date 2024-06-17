import unittest

class TestScheduler(unittest.TestCase):
    def test_is_available(self):
        self.assertTrue(is_available("MWF 9:00-10:00"))

if __name__ == '__main__':
    unittest.main()
