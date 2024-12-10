import unittest


class TestNone(unittest.TestCase):
    def test_inclusion(self):
        self.assertIn("k", "king")  # self.assertTrue("k" in "king")
        self.assertIn(1, [1, 4, 5])
        self.assertIn(5, (3, 5, 4))
        self.assertIn("a", {"a": 1, "b": 3})
        self.assertIn("2", {"a": 1, "b": 2}.values())

    def test_exclusion(self):
        self.assertNotIn("a", "king")  # self.assertTrue("k" in "king")
        self.assertNotIn(8, [1, 4, 5])
        self.assertNotIn(2, (3, 5, 4))
        self.assertNotIn("c", {"a": 1, "b": 3})
        self.assertNotIn("5", {"a": 1, "b": 2}.values())


if __name__ == "__main__":
    unittest.main()
