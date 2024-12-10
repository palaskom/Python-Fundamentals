import unittest


class ObjectTypeTest(unittest.TestCase):
    def test_is_instance(self):
        self.assertIsInstance(1, int)
        self.assertIsInstance(4.3, float)
        self.assertIsInstance([], list)
        self.assertIsInstance({"a": 1, "b": 2}, dict)

    def test_not_is_instance(self):
        self.assertNotIsInstance(1, float)
        self.assertNotIsInstance(4.3, dict)
        self.assertNotIsInstance([], float)
        self.assertNotIsInstance({"a": 1, "b": 2}, list)


if __name__ == "__main__":
    unittest.main()
