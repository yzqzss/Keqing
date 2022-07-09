import unittest

from tests.test_iterator import TestIterator
from tests.test_load import TestLoad

if __name__ == "__main__":
    suite=unittest.TestSuite()
    suite.addTest(TestLoad("test_load_OSMWebsite"))
    suite.addTest(TestLoad("test_load_JOSM"))
    suite.addTest(TestLoad("test_load_level0"))
    suite.addTest(TestIterator("test_iterator_node"))
    runner=unittest.TextTestRunner()
    runner.run(suite)