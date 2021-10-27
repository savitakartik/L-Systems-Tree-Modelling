import unittest
import argsChecker

class argsCheckerTest(unittest.TestCase):
    """
    Tests the :class:`argsChecker` class.
    """
    def test_check_iter(self):

        with self.assertRaises(TypeError):
            self.checkIter(0)


