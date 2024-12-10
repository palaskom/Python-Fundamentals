import unittest


class TestStringMethods(unittest.TestCase):
    def test_split(self):
        self.assertEqual("a-b-c".split("-"), ["a", "b", "c"])
        # self.assertEqual("d+e+f".split("+"), ["d", "e", "f"])

    def test_count(self):
        self.assertEqual("beautiful".count("u"), 2)

    def test_swapcase(self):
        self.assertEqual("aBcD".swapcase(), "AbCd")

    def test_index(self):
        self.assertEqual("abcd".index("c"), 2)


if __name__ == "__main__":
    unittest.main()
