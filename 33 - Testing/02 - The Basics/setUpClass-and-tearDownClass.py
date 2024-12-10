import unittest


class TestOperations(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("This will run ONCE BEFORE the test suite starts")

    def setUp(self):
        print("This will run BEFORE EACH test")

    def tearDown(self):
        print("This will run AFTER EACH test")

    @classmethod
    def tearDownClass(cls):
        print("This will run ONCE AFTER the test suite starts")

    def test_stuff(self):
        self.assertEqual(1, 1)

    def test_more_stuff(self):
        self.assertEqual([], [])


if __name__ == "__main__":
    unittest.main()
