import unittest

from slugify import slugify


class SlugifyTests(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(slugify("Hello World"), "hello-world")

    def test_punctuation_removed(self):
        self.assertEqual(slugify("Hello, World!"), "hello-world")

    def test_surrounding_space_trimmed(self):
        self.assertEqual(slugify("  Hello World  "), "hello-world")


if __name__ == "__main__":
    unittest.main()
